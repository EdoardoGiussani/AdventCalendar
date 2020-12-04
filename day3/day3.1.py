class Pos:
    row=0
    col=0

    def __init__(self, lines):
        self.lines = lines.copy()
        self.lineCount = len(lines)
        self.lineLength = len(lines[0])

    def NextPosition(self):
        self.row = self.row + 1
        if self.row >= self.lineCount:
            return False
        self.col = self.col + 3
        if self.col >= self.lineLength:
            self.col = self.col - self.lineLength
        return True

    def IsTree(self):
        patch = self.lines[self.row][self.col]
        if patch == '#':
            self.lines[self.row][self.col] = 'X'
            return True
        else:
            self.lines[self.row][self.col] = 'O'
            return False

    def Print(self):
        for line in self.lines:
            line = "".join(line)
            print(line)


def GetLines():
    file = open("day3/entries.txt")
    entries = file.readlines()
    for i in range(len(entries)):
        entries[i] = list(entries[i].rstrip())
    return entries

lines = GetLines()
pos = Pos(lines)
treeCount = 0
while (pos.NextPosition()):
    if pos.IsTree():
        treeCount = treeCount + 1
pos.Print()
print("{}, {}; TreeCount = {}".format(pos.lineLength, pos.lineCount, treeCount))