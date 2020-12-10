def GetLines():
    file = open("day10/entries.txt")
    entries = file.readlines()
    for i in range(len(entries)):
        entries[i] = int(entries[i])
    return entries

numbers = GetLines()
numbers.sort()

oneJump = 0
threeJump = 1
lastNum = 0

for num in numbers:
    diff = num - lastNum
    if diff == 1:
        oneJump = oneJump + 1
    if diff == 3:
        threeJump = threeJump + 1
    lastNum = num

print('{}*{}={}'.format(oneJump, threeJump, oneJump*threeJump))