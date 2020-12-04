def GetNumbersList():
    file = open("day1/entries.txt")
    entries = file.readlines()
    for i in range(len(entries)):
        entries[i] = int(entries[i])
    print(entries)
    return entries

def FindNums(entries):
    for i in range(len(entries)):
        for y in range(i, len(entries)):
            for z in range(len(entries)):
                if entries[i] + entries[y] + entries [z]== 2020:
                    print (entries[i], entries[y], entries[z])
                    return (entries[i], entries[y], entries[z])


entries = GetNumbersList()
nums = FindNums(entries)
print(nums[0]*nums[1]*nums[2])