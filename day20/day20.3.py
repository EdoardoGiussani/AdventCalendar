import re

def GetLines():
    with open("day20\\image.txt") as f:
        entries = f.readlines()
    image = list()
    for line in entries:
        image.append(line.strip())
    return image

def GetColumn(tile, column):
    border = ''
    for i in range(len(tile)):
        border += tile[i][column]
    return list(border)


def FindMonster_old(image):
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


def FindMonster(image):
    monsters = 0
    i = 1
    monsterMiddle = re.compile('#....##....##....###')
    monsterLow =    re.compile('.#..#..#..#..#..#...')
    while i < len(image) - 1:
        middleMatches = monsterMiddle.finditer(image[i])
        lowMatches = monsterLow.finditer(image[i + 1])
        for midMatch in middleMatches:
            # print(midMatch.start())
            for lowMatch in lowMatches:
                # print(lowMatch.start())
                if midMatch.start() == lowMatch.start():
                    if image[i - 1][lowMatch.start() + 1] == '#':
                        print('line: {}, index: {}'.format(i, lowMatch.start()))
                        monsters += 1
        i += 1
    return monsters

def RotateImage(image):
    rotated_image = list()
    for i in range(len(image)):
        rotated_image.append(GetColumn(image, i)[::-1])
    return MergeLines(rotated_image)
    
def FlipImage(image, flip_vertical):
    flipped_image = list()
    if flip_vertical:
        flipped_image = image[::-1]
    else:
        for line in image:
            flipped_image.append(line[::-1])
    return MergeLines(flipped_image)

def PrintTile(tile_content):
    return
    for line in tile_content:
        print(''.join(line))
    print()
    print()

def MergeLines(image):
    for i in range(len(image)):
        line = ''.join(image[i])
        image[i] = line
    return image

def AnalyzeImage(image):
    monsters = 0
    i = 0
    while i < 3:
        PrintTile(image)
        monsters += FindMonster(image)
        # if monsters != 0:
        #     break

        image = FlipImage(image, True)
        PrintTile(image)
        monsters += FindMonster(image)
        # if monsters != 0:
        #     break
        image = FlipImage(image, False)
        PrintTile(image)
        monsters += FindMonster(image)
        # if monsters != 0:
        #     break
        image = FlipImage(image, True)
        PrintTile(image)
        monsters += FindMonster(image)
        # if monsters != 0:
        #     break

        image = FlipImage(image, False)
        image = RotateImage(image)
        i += 1

    return monsters

def CountHashTag(image):
    counter = 0
    for line in image:
        for c in line:
            if c == '#':
                counter += 1
    return counter

if __name__ == "__main__":
    image = GetLines()
    monsters = AnalyzeImage(image)
    hashtags = CountHashTag(image)
    result = hashtags - (15 * monsters)
    print(result)
