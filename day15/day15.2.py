def GetLines():
    with open("day15\\entries.txt") as f:
        entries = f.readlines()
        for i in range(len(entries)):
            sequence = entries[i].split(',')
            for j in range(len(sequence)):
                sequence[j] = int(sequence[j])
            entries[i] = sequence
    return entries

def PlayGame(numbers, turns):
    nums = {}
    for i in range(len(numbers) - 1):
        nums[numbers[i]] = i
    num = numbers[-1]
    for turn in range(len(nums) + 1, turns):
        lastNum = num
        if lastNum not in nums:
            num = 0
        else:
            num = turn - 1 - nums[lastNum]
        nums[lastNum] = turn - 1
        # if turn % 10000 == 0:
        #     print('{}: {}'.format(turn, num))
    return turn, num

def FindLastOccurrence(nums, num):
    return len(nums) - 1 - nums[::-1].index(num)

if __name__ == "__main__":
    entries = GetLines()
    for sequence in entries:
        turn, number = PlayGame(sequence, 30000000)
        print('Sequence: {}; Turn: {}; Result: {}'.format(sequence, turn + 1, number))