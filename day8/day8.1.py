def GetLines():
    file = open("day8/entries.txt")
    entries = file.readlines()
    return entries



instructions = GetLines()

accumulator = 0
index = 0
executed = list()

while index not in executed:
    executed.append(index)
    instruction = instructions[index].split(' ')
    instruction[1] = int(instruction[1])
    if instruction[0] == 'acc':
        accumulator = accumulator + instruction[1]
        index = index + 1
    if instruction[0] == 'jmp':
        index = index + instruction[1]
    if instruction[0] == 'nop':
        index = index + 1


print(accumulator, index)