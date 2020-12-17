def GetLines():
    with open("day17\\entries.txt") as f:
        entries = f.readlines()
    for i in range(len(entries)):
        entries[i] = entries[i].rstrip()
    return entries

def CreateEnergySource(firstLayer):
    cubes = {}
    for y in range(len(firstLayer)):
        for x in range(len(firstLayer)):
            cubes[(x, y, 0, 0)] = firstLayer[y][x] == '#'
            CountActivesNear(cubes.copy(), cubes, (x, y, 0, 0))
    return cubes
    
def CountActivesNear(oldCubes, cubes, coordinates):
    actives = 0
    near = range(-1,2)
    for i in near:
        x = coordinates[0] + i
        for j in near:
            y = coordinates[1] + j
            for k in near:
                z = coordinates[2] + k
                for n in near:
                    w = coordinates[3] + n
                    if not (i == j == k == n == 0):
                        if (x, y, z, w) in oldCubes:
                            if oldCubes[(x, y, z, w)]:
                                actives += 1
                        else:
                            cubes[(x, y, z, w)] = False
    return actives

def NewStatus(status, nearActives):
    if status:
        if not (nearActives == 2 or nearActives == 3):
            return False
    else:
        if nearActives == 3:
            return True
    return None

def NextCycle(cubes):
    oldCubes = cubes.copy()
    for cube in oldCubes:
        nearActive = CountActivesNear(oldCubes, cubes, cube)
        newStatus = NewStatus(oldCubes[cube], nearActive)
        if newStatus != None:
            cubes[cube] = newStatus

def CountActives(cubes):
    actives = 0
    for cube in cubes:
        if cubes[cube]:
            actives += 1
    return actives

if __name__ == "__main__":
    entries = GetLines()
    cubes = CreateEnergySource(entries)
    cycle = 0
    while cycle < 6:
        print(cycle, CountActives(cubes))
        NextCycle(cubes)
        cycle += 1
    print(cycle, CountActives(cubes))
