class Pos:
    row=0
    col=0
    treeCount = 0

    def __init__(self, down, right):
        self.lines = self.GetLines()
        self.lineCount = len(self.lines)
        self.lineLength = len(self.lines[0])
        self.down = down
        self.right = right
        self.CountTree()

    def NextPosition(self):
        self.row = self.row + self.down
        if self.row >= self.lineCount:
            return False
        self.col = self.col + self.right
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

    def CountTree(self):
        while (self.NextPosition()):
            if self.IsTree():
                self.treeCount = self.treeCount + 1
        return self.treeCount

    def PrintPath(self):
        for line in self.lines:
            line = "".join(line)
            print(line)
        self.PrintInfo()

    def PrintInfo(self):
        print("Down: {}; Right: {}; Trees: {}".format(self.down, self.right, self.treeCount))


    def GetLines(self):
        file = open("day3/entries.txt")
        entries = file.readlines()
        for i in range(len(entries)):
            entries[i] = list(entries[i].rstrip())
        return entries

one = Pos(1, 1)
two = Pos(1, 3)
three = Pos(1, 5)
four = Pos(1, 7)
five = Pos(2, 1)

two.PrintPath()

one.PrintInfo()
two.PrintInfo()
three.PrintInfo()
four.PrintInfo()
five.PrintInfo()

print(one.treeCount * two.treeCount * three.treeCount * four.treeCount * five.treeCount)