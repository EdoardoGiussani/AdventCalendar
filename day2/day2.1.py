def GetLines():
    file = open("day2/entries.txt")
    entries = file.readlines()
    return entries

class PasswordModel:
    Password = ""
    Char = ''
    MinOccurence = 0
    MaxOccurence = 0

    def __init__(self, string):
        strings = string.split(" ")
        self.Password = strings[2].rstrip()
        self.Char = strings[1][0]
        nums = strings[0].split("-")
        self.MinOccurence = int(nums[0])
        self.MaxOccurence = int(nums[1])
        print("{}, {}, {}, {}: {}".format(self.Password, self.Char, self.MinOccurence, self.MaxOccurence, self.IsValid()))

    def IsValid(self):
        count = 0
        for i in self.Password:
            if i == self.Char:
                count = count + 1
        return self.MinOccurence <= count & count <= self.MaxOccurence


counter = 0
lines = GetLines()
for i in range(len(lines)):
    psw = PasswordModel(lines[i])
    if psw.IsValid() == True:
        counter = counter + 1
print (counter)