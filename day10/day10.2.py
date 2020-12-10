def GetLines():
    file = open("day10\\entries.txt")
    entries = file.readlines()
    for i in range(len(entries)):
        entries[i] = int(entries[i])
    return entries

def GetCombinations(nums, index):
    nums = nums.copy()
    if not IsValid(nums):
        return 0
    if index >= len(nums) - 1:
        print(nums)
        return 1

    combinations = 0
    combinations = combinations + GetCombinations(nums, index + 1)
    nums.pop(index)
    combinations = combinations + GetCombinations(nums, index)
    return combinations
        
def IsValid(nums):
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] > 3:
            return False
    return True
        


numbers = GetLines()
numbers.append(max(numbers) + 3)
numbers.append(0)
numbers.sort()
print(numbers)
lastNum = 0
combCounter = 1

i = 0
while i < len(numbers) - 1:
    nextNums = list()
    nextNums.append(numbers[i])
    i = i + 1
    while numbers[i] - numbers[i-1] < 3:
        nextNums.append(numbers[i])
        i = i + 1
        if i >= len(numbers):
            break
    combinations = GetCombinations(nextNums, 1)
    combCounter = combCounter * combinations
    print('{}: {}'.format(nextNums, combinations))
print(combCounter)