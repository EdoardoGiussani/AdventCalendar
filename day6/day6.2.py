def GetLines():
    file = open("day6/entries.txt")
    entries = file.readlines()
    for i in range(len(entries)):
        entries[i] = entries[i].rstrip()
    return entries

def CountAnswers(answers, people):
    uniqueAnswers = list()
    everyone = 0

    for c in answers:
        if c not in uniqueAnswers:
            uniqueAnswers.append(c)

    for c in uniqueAnswers:
        if answers.count(c) == people:
            everyone = everyone + 1
    return everyone



lines = GetLines()
totalAns = 0
groupAns = ''
groupCount = 0

for line in lines:
    if line == '':
        totalAns = totalAns + CountAnswers(groupAns, groupCount)
        groupAns = ''
        groupCount = 0
    else:
        groupAns = groupAns + line
        groupCount = groupCount + 1
        
totalAns = totalAns + CountAnswers(groupAns, groupCount)

print(totalAns)