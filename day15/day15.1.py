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
    nums = numbers.copy()
    for turn in range(len(nums), turns):
        lastNum = nums[-1]
        if lastNum not in nums[:-1]:
            num = 0
        else:
            num = turn - 1 - FindLastOccurrence(nums[:-1], lastNum)
        nums.append(num)
        #print('{}: {}'.format(turn, num))
    return turn, num

def FindLastOccurrence(nums, num):
    return len(nums) - 1 - nums[::-1].index(num)

if __name__ == "__main__":
    entries = GetLines()
    for sequence in entries:
        turn, number = PlayGame(sequence, 2020)
        print('Sequence: {}; Turn: {}; Result: {}'.format(sequence, turn + 1, number))