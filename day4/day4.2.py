import re

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
    if not IsValidByr(passaport['byr']):
        print('Invalid byr: {}'.format(passaport['byr']))
        return False
    if not IsValidIyr(passaport['iyr']):
        print('Invalid iyr: {}'.format(passaport['iyr']))
        return False
    if not IsValidEyr(passaport['eyr']):
        print('Invalid eyr: {}'.format(passaport['eyr']))
        return False
    if not IsValidHgt(passaport['hgt']):
        print('Invalid hgt: {}'.format(passaport['hgt']))
        return False
    if not IsValidHcl(passaport['hcl']):
        print('Invalid hcl: {}'.format(passaport['hcl']))
        return False
    if not IsValidEcl(passaport['ecl']):
        print('Invalid ecl: {}'.format(passaport['ecl']))
        return False
    if not IsValidPid(passaport['pid']):
        print('Invalid pid: {}'.format(passaport['pid']))
        return False
    return True

def IsValidByr(value):
    value = int(value)
    return 1920 <= value <= 2002

def IsValidIyr(value):
    value = int(value)
    return 2010 <= value <= 2020

def IsValidEyr(value):
    value = int(value)
    return 2020 <= value <= 2030

def IsValidHgt(value):
    unit = value[-2:]
    value = int(value [:-2])
    if unit == 'cm':
        return 150 <= value <= 193
    if unit == 'in':
        return 59 <= value <= 76
    return False

def IsValidHcl(value):
    match = re.search('^#[0-9a-f]{6}$', value)
    return match is not None

def IsValidEcl(value):
    eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return value in eyeColors

def IsValidPid(value):
    match = re.search('^\d{9}$', value)
    return match is not None


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
    #else:
        #print("Non-Valid: {}".format(psprt))

print(validCounter)