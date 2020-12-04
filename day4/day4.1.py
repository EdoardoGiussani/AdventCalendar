def StringToDict(infoString):
    passaport={}
    infoString = str(infoString)
    infos = infoString.split(' ')
    for i in range(len(infos)):
        info = infos[i].split(':')
        passaport[info[0]] = info[1]
    return passaport

def IsValidPassaport(passaport):
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    ignorableFields = ['cid']
    for field in requiredFields:
        if not field in passaport:
            return False
    return True

def GetLines():
    file = open("day4/entries.txt")
    entries = file.readlines()
    for i in range(len(entries)):
        entries[i] = entries[i].rstrip()
    return entries

validCounter = 0
lines = GetLines()
for line in lines:
    psprt = StringToDict(line)
    if IsValidPassaport(psprt):
        validCounter = validCounter + 1
        print("Valid: {}".format(psprt))
    else:
        print("Non-Valid: {}".format(psprt))

print(validCounter)