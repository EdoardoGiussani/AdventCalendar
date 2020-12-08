def GetLines():
    file = open("day8/entries.txt")
    entries = file.readlines()
    return entries

def TryPath(instructions, executed, index):
    executed = executed.copy()
    accumulator = 0
    
    while index not in executed:
        if index == len(instructions):
            return True, accumulator
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
    return False, 0


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
        IsCorrect, accCharge = TryPath(instructions, executed, index + 1)
        if IsCorrect:
            accumulator = accumulator + accCharge
            break
        else:
            index = index + instruction[1]
    if instruction[0] == 'nop':
        IsCorrect, accCharge = TryPath(instructions, executed, index + instruction[1])
        if IsCorrect:
            accumulator = accumulator + accCharge
            break
        else:
            index = index + 1


print(accumulator)