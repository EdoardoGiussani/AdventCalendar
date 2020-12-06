def GetLines():
    file = open("day6/entries.txt")
    entries = file.readlines()
    for i in range(len(entries)):
        entries[i] = entries[i].rstrip()
    return entries

def CountAnswers(answers):
    uniqueAnswers = list()
    for c in answers:
        if c not in uniqueAnswers:
            uniqueAnswers.append(c)
    return len(uniqueAnswers)



lines = GetLines()
totalAns = 0
groupAns = ''
for line in lines:
    if line == '':
        totalAns = totalAns + CountAnswers(groupAns)
        groupAns = ''
    else:
        groupAns = groupAns + line
        
totalAns = totalAns + CountAnswers(groupAns)

print(totalAns)