def GetLines():
    file = open("day9/entries.txt")
    entries = file.readlines()
    for i in range(len(entries)):
        entries[i] = int(entries[i])
    return entries

def IsValid(num, preamble):
    for i in range(len(preamble)):
        for s in range(i + 1, len(preamble)):
            if preamble[i] + preamble[s] == num:
                return True
    return False

def GetValues(index, numbers):
    number = numbers[index]
    preamble = numbers[index - 25: index]
    return number, preamble

numbers = GetLines()
index = 25
number, preamble = GetValues(index, numbers)

while IsValid(number, preamble):
    index = index + 1
    number, preamble = GetValues(index, numbers)

index = 0
rangeLen = 2
while True:
    addends = numbers[index:index + rangeLen]
    mySum = sum(addends)
    if mySum == number:
        break
    elif mySum > number:
        index = index + 1
        rangeLen = 2
    else:
        rangeLen = rangeLen + 1

minAdd = min(addends)
maxAdd = max(addends)

result = minAdd + maxAdd

print(number, result)