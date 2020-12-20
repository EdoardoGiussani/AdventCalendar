import re

def GetLines():
    with open("day20\\entries.txt") as f:
        entries = f.readlines()
    return entries

def PrintOrderedTiles(orderedTiles):
    for level in orderedTiles:
        for i in range(len(level[0])):
            line = ''
            for tile in level:
                line += ''.join(tile[i])
                line += ' '
            print(line)
        print()
    print()

def PrintTile(tile_content):
    for line in tile_content:
        print(''.join(line))
    print()

def ConvertToTiles(entries):
    tiles = {}
    tileContent = list()

    for line in entries:
        if line == '\n':
            tile = {
                'content': tileContent,
                'borders': GetBorders(tileContent)
            }
            tiles[tileId] = tile
            tileContent = list()

        elif line.startswith('Tile '):
            tileId = line[line.index(' ') : line.index(':')]
            tileId = int(tileId)

        else:
            tileContent.append(list(line.strip()))

    tile = {
        'content': tileContent,
        'borders': GetBorders(tileContent)
    }
    tiles[tileId] = tile
    return tiles

def GetBorders(tile):
    borders = list()
    borders.append(tile[0])
    borders.append(GetColumn(tile, -1))
    borders.append(tile[-1])
    borders.append(GetColumn(tile, 0))
    return borders
    
def GetColumn(tile, column):
    border = ''
    for i in range(len(tile)):
        border += tile[i][column]
    return list(border)

def FindAdjacentTile(tiles, tile_id, border):
    for tile in tiles:
        if tile == tile_id:
            continue
        borders = tiles[tile]['borders']
        if border in borders: 
            return tile, borders.index(border), False
        elif border[::-1] in borders:
            return tile, borders.index(border[::-1]), True
    return None, None, None

def GetAdjacentTiles(tiles, tile_id):
    adjacentTiles = list()
    borders = tiles[tile_id]['borders']
    for border in borders:
        adjacent, direction, flipped = FindAdjacentTile(tiles, tile_id, border)
        if adjacent is not None:
            adjacentTiles.append((tile_id, borders.index(border), adjacent, direction, flipped))
    return adjacentTiles

def RotateFirstCorner(tiles, tile_id, aligments):
    als = (aligments[0][1], aligments[1][1])
    minAl = min(als)
    if minAl == 0 and max(als) == 3:
        minAl = 3
    while minAl != 1:
        tiles = RotateTile(tiles, tile_id)
        minAl += 1
        if minAl == 4:
            minAl = 0
    return tiles

def AllignTiles(tiles, tile_alignment):
    tile_1_id = tile_alignment[0]
    border_1_id = tile_alignment[1]
    tile_2_id = tile_alignment[2]
    border_2_id = tile_alignment[3]

    if border_1_id == 0:
        target_border = 2
    elif border_1_id == 1:
        target_border = 3
    elif border_1_id == 2:
        target_border = 0
    elif border_1_id == 3:
        target_border = 1

    while target_border != border_2_id:
        tiles = RotateTile(tiles, tile_2_id)
        border_2_id += 1
        if border_2_id == 4:
            border_2_id = 0

    inverted_border_1 = tiles[tile_1_id]['borders'][border_1_id][::-1]
    border_2 = tiles[tile_2_id]['borders'][border_2_id]
    if inverted_border_1 == border_2:
        if border_2_id in (0,2):
            tiles = FlipTile(tiles, tile_2_id, False)
        else:
            tiles = FlipTile(tiles, tile_2_id, True)
    return tiles

def RotateTile(tiles, tile_id):
    tile_content = tiles[tile_id]['content']
    rotated_content = list()
    for i in range(len(tile_content)):
        rotated_content.append(GetColumn(tile_content, i)[::-1])
    tiles[tile_id]['content'] = rotated_content
    tiles[tile_id]['borders'] = GetBorders(rotated_content)
    return tiles

def FlipTile(tiles, tile_id, flip_vertical):
    tile_content = tiles[tile_id]['content']
    flipped_content = list()
    if flip_vertical:
        flipped_content = tile_content[::-1]
    else:
        for line in tile_content:
            flipped_content.append(line[::-1])
    tiles[tile_id]['content'] = flipped_content
    tiles[tile_id]['borders'] = GetBorders(flipped_content)
    return tiles

def OrderTiles(tiles):
    for tile in tiles:
        aligments = GetAdjacentTiles(tiles, tile)
        if len(aligments) == 2:
            tiles = RotateFirstCorner(tiles, tile, aligments)
            break

    orderedTiles = list()
    level = 0

    aligments = GetAdjacentTiles(tiles, tile)
    down = DownTile(aligments)
    while down is not None:

        orderedTiles.append(list())
        orderedTiles[level].append(tiles[tile]['content'])
        # PrintOrderedTiles(orderedTiles)

        firstDown = DownTile(aligments)
        right = RightTile(aligments)

        while right is not None:
            tiles = AllignTiles(tiles, right)
            alignedTile = tiles[right[2]]

            orderedTiles[level].append(alignedTile['content'])
            # PrintOrderedTiles(orderedTiles)

            aligments = GetAdjacentTiles(tiles, right[2])
            right = RightTile(aligments)

        if firstDown is None:
            break
        tiles = AllignTiles(tiles, firstDown)
        tile = firstDown[2]

        aligments = GetAdjacentTiles(tiles, tile)
        down = firstDown
        level += 1
    return orderedTiles

def RightTile(aligments):
    for al in aligments:
        if al[1] == 1:
            return al
    return None

def DownTile(aligments):
    for al in aligments:
        if al[1] == 2:
            return al
    return None

def TrimTiles(tiles):
    trimmed = list()
    for level in range(len(tiles)):
        trimmed.append(list())
        for tile in tiles[level]:
            trimmedTile = list()
            for line in tile[1:-1]:
                trimmedTile.append(line[1:-1])
            trimmed[level].append(trimmedTile)
    return trimmed

def MergeTiles(tiles):
    mergedTiles = list()
    for level in tiles:
        for i in range(len(level[0])):
            line = ''
            for tile in level:
                line += ''.join(tile[i])
            mergedTiles.append(line)
    return mergedTiles

def FindMonster(image):
    monsters = 0
    i = 1
    monsterHead =   '..................#.'
    monsterMiddle = '#....##....##....###'
    monsterLow =    '.#..#..#..#..#..#...'
    while i < len(image) - 1:
        headMatches = re.findall(monsterHead, image[i - 1])
        middleMatches = re.findall(monsterMiddle, image[i])
        lowMatches = re.findall(monsterLow, image[i + 1])
        if headMatches and middleMatches and lowMatches:
            for midMatch in middleMatches:
                midIndex = ''.join(image[i]).find(midMatch)
                for lowMatch in lowMatches:
                    lowIndex = ''.join(image[i + 1]).find(lowMatch)
                    if lowIndex == midIndex:
                        if image[i - 1][midIndex + 19] == '#':
                            monsters += 1
        i += 1
    return monsters

def RotateImage(image):
    rotated_image = list()
    for i in range(len(image)):
        rotated_image.append(GetColumn(image, i)[::-1])
    return MergeLines(rotated_image)
    

def MergeLines(image):
    for i in range(len(image)):
        line = ''.join(image[i])
        image[i] = line
    return image

def AnalyzeImage(image):
    monsters = 0
    PrintTile(image)
    monsters += FindMonster(image)
    print('Monsters:', monsters)
    return monsters

def CountHashTag(image):
    counter = 0
    for line in image:
        for c in line:
            if c == '#':
                counter += 1
    return counter

if __name__ == "__main__":
    entries = GetLines()
    tiles = ConvertToTiles(entries)
    orderedTiles = OrderTiles(tiles)
    PrintOrderedTiles(orderedTiles)
    trimmedTiles = TrimTiles(orderedTiles)
    PrintOrderedTiles(trimmedTiles)
    image = MergeTiles(trimmedTiles)
    PrintTile(image)
    with open('day20\\image.txt', 'w') as f:
        for line in image:
            f.write(line)
            f.write('\n')
    monsters = 0
    while monsters == 0:
        monsters = AnalyzeImage(image)
        image = RotateImage(image)
        image = MergeLines(image)
    result = CountHashTag(image)
    result -= 15 * monsters
    print(result)
