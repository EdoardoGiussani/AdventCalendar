def GetPasswords():
    with open("day2/passwords.txt") as f:
        lines = f.readlines()
        passwords = list()
        for line in lines:
            passwords.append(StringToPassword(line))
    return passwords

def StringToPassword(string):
    strings = string.split(' ')
    nums = strings[0].split('-')
    password = {}
    password['pswrd'] = strings[2].rstrip()
    password['char'] = strings[1][0]
    password['min'] = int(nums[0])
    password['max'] = int(nums[1])
    return password

def IsValidPassword(pswrd):
    char1 = pswrd['pswrd'][pswrd['min'] - 1]
    char2 = pswrd['pswrd'][pswrd['max'] - 1]
    return (char1 == pswrd['char']) != (char2 == pswrd['char'])

if __name__ == "__main__":
    passwords = GetPasswords()
    validPswrds = [pswrd for pswrd in passwords if IsValidPassword(pswrd)]
    print ('There are {} valid passwords in your input'.format(len(validPswrds)))