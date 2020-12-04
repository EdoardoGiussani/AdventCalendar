def GetLines():
    file = open("day2/entries.txt")
    entries = file.readlines()
    return entries

class PasswordModel:
    Password = ""
    Char = ''
    FirstChar = ''
    SecondChar = ''

    def __init__(self, string):
        strings = string.split(" ")
        self.Password = strings[2].rstrip()
        self.Char = strings[1][0]
        nums = strings[0].split("-")
        self.FirstChar = self.Password[int(nums[0])-1]
        self.SecondChar = self.Password[int(nums[1])-1]
        print("{}, {}, {}, {}: {}".format(self.Password, self.Char, self.FirstChar, self.SecondChar, self.IsValid()))

    def IsValid(self):
        if self.FirstChar == self.Char:
            if self.SecondChar != self.Char:
                return True
        else:
            if self.SecondChar == self.Char:
                return True
        return False


counter = 0
lines = GetLines()
for i in range(len(lines)):
    psw = PasswordModel(lines[i])
    if psw.IsValid() == True:
        counter = counter + 1
print (counter)