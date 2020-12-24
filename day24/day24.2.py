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

def CountBlackAdjacent(old_floor, tile, floor):
    directions = GetDirections()
    black_count = 0
    for dir in directions:
        direction = directions[dir]
        coordinates = (tile[0] + direction[0], tile[1] + direction[1])
        if coordinates not in old_floor:
            floor[coordinates] = False
        else:
            if old_floor[coordinates]:
                black_count += 1
    return black_count, floor

def FlipTile(old_floor, tile, floor):
    black_adjacent, floor = CountBlackAdjacent(old_floor, tile, floor)
    if old_floor[tile]:
        if black_adjacent == 0 or black_adjacent > 2:
            floor[tile] = False
    else:
        if black_adjacent == 2:
            floor[tile] = True
    return floor

def FlipTiles(floor):
    old_floor = floor.copy()
    for tile in old_floor:
        floor = FlipTile(old_floor, tile, floor)
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
    print('-- Day 0 --\nRegistered tiles: {}, black tiles: {}'.format(len(floor), result))
    old_floor = floor.copy()
    for tile in old_floor:
        _, floor = CountBlackAdjacent(old_floor, tile, floor)
    for day in range(100):
        floor = FlipTiles(floor)
        print('-- Day {} --\nBalck tiles: {}'.format(day + 1, CountBlacks(floor)))

