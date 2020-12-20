import math

def GetLines():
    with open("day20\\entries.txt") as f:
        entries = f.readlines()
    return entries

def ConvertToTiles(entries):
    tiles = {}
    tileContent = list()
    for line in entries:
        if line == '\n':
            tiles[tileId] = tileContent
            tileContent = list()
        elif line.startswith('Tile '):
            tileId = line[line.index(' ') : line.index(':')]
            tileId = int(tileId)
        else:
            tileContent.append(line.strip())
    if tileId not in tiles:
        tiles[tileId] = tileContent
    return tiles

def GetBorders(tile):
    borders = list()
    borders.append(tile[0])
    borders.append(tile[-1])
    borders.append(GetVerticalBorder(tile, 0))
    borders.append(GetVerticalBorder(tile, -1))
    # borders += FlipBorders(borders)
    return borders
    
def GetVerticalBorder(tile, column):
    border = ''
    for i in range(len(tile)):
        border += tile[i][column]
    return border

def FlipBorders(borders):
    flipped = list()
    for border in borders:
        flipped.append(border[::-1])
    return flipped

def CountMatchingBorders(borders, tileId):
    count = 0
    for matchTile in borders:
        if matchTile == tileId:
            continue
        for border in borders[tileId]:
            if border in borders[matchTile] or border[::-1] in borders[matchTile]:
                count += 1
                if count == 4:
                    return count
                break
    return count
        

if __name__ == "__main__":
    entries = GetLines()
    tiles = ConvertToTiles(entries)
    borders = {}
    for tile in tiles:
        borders[tile] = GetBorders(tiles[tile])
    
    corners = list()
    for tile in borders:
        if CountMatchingBorders(borders, tile) == 2:
            corners.append(tile)
    print(corners)
    print(math.prod(corners))
