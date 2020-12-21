import re

def GetLines():
    with open("day20\\image.txt") as f:
        entries = f.readlines()
    image = list()
    for line in entries:
        image.append(line.strip())
    return image

def GetColumn(image, column):
    border = ''
    for i in range(len(image)):
        border += image[i][column]
    return list(border)

def SearchForMonster(image, i):
    monsters = 0
    headLine = image[i - 1]
    bodyLine = image[i]
    bottomLine = image[i + 1]
    
    head = (18, 18)
    body = (0,5,6,11,12,17,18,19)
    bottom = (1,4,7,10,13,16)

    for i in range(len(bodyLine) - 20):
        if SearchMonsterPart(bodyLine[i:], body):
            if SearchMonsterPart(bottomLine[i:], bottom):
                if SearchMonsterPart(headLine[i:], head):
                    monsters += 1
    return monsters

def SearchMonsterPart(line, part):
    for pos in part:
        if not line[pos] == '#':
            return False
    return True

def FindMonster(image):
    monsters = 0
    for i in range(len(image) - 1):
        monsters += SearchForMonster(image, i)
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
        if monsters != 0:
            break

        image = FlipImage(image, True)
        PrintTile(image)
        monsters += FindMonster(image)
        if monsters != 0:
            break
        image = FlipImage(image, False)
        PrintTile(image)
        monsters += FindMonster(image)
        if monsters != 0:
            break
        image = FlipImage(image, True)
        PrintTile(image)
        monsters += FindMonster(image)
        if monsters != 0:
            break

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
