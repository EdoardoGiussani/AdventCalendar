def GetLines():
    with open("day24\\entries.txt") as f:
        entries = f.read().split('\n')
    return entries

def ParseTrack(path_string):
    path = list()
    i = 0
    while i < len(path_string):
        c = path_string[i]
        if c == 's' or c == 'n':
            i += 1
            c += path_string[i]
        path.append(c)
        i += 1
    return path

def GetDirections():
    return {
        'e':  ( 2,  0),
        'se': ( 1, -1),
        'sw': (-1, -1),
        'w':  (-2,  0),
        'nw': (-1,  1),
        'ne': ( 1,  1),
    }

def ParseEntries(entries):
    paths = list()
    for entry in entries:
        paths.append(ParseTrack(entry))
    return paths

def FollowPaths(floor, paths):
    for path in paths:
        floor = FollowPath(floor, path)
    return floor

def FollowPath(floor, path):
    coordinates = [0,0]
    directions = GetDirections()
    for move in path:
        direction = directions[move]
        coordinates[0] += direction[0]
        coordinates[1] += direction[1]
    coordinates = tuple(coordinates)
    if coordinates not in floor:
        floor[coordinates] = True
    else:
        floor[coordinates] = not floor[coordinates]
    return floor

def CountBlacks(floor):
    count = 0
    for tile in floor:
        if floor[tile]:
            count += 1
    return count

if __name__ == "__main__":
    entries = GetLines()
    paths = ParseEntries(entries)

    floor = {
        (0,0): False
    }
    floor = FollowPaths(floor, paths)
    result = CountBlacks(floor)
    print('Registered tiles: {}, black tiles: {}'.format(len(floor), result))
