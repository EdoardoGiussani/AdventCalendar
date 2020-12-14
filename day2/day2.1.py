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
    chars = [char for char in pswrd['pswrd'] if char == pswrd['char']]
    return pswrd['min'] <= len(chars) <= pswrd['max']

if __name__ == "__main__":
    passwords = GetPasswords()
    validPswrds = [pswrd for pswrd in passwords if IsValidPassword(pswrd)]
    print ('There are {} valid passwords in your input'.format(len(validPswrds)))