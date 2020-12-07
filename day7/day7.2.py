class Bag:
    def __init__(self, inputStr):
        inputs = inputStr.split('contain')
        self.Color = self._getBagColor(inputs[0])
        self.Contain = list()
        contains = inputs[1].split(',')
        for bag in contains:
            bag = bag.strip()
            self.Contain.append(self._getBagColor(bag))

    def GetContainBagCount(self, bags):
        totalCount = 0
        if self.Contain[0] == 'no other':
            return 0
        for bagColor in self.Contain:
            bag = [x for x in bags if x.Color == bagColor[0]][0]
            count = (bag.GetContainBagCount(bags) +1)* bagColor[1]
            totalCount = totalCount + count
        return totalCount


    def _getBagColor(self, string):
        bagIndex = string.find(' bag')
        if string[0].isdigit():
            countIndex = string.find(' ')
            bagCount = string[:countIndex]
            string = string[countIndex:]
            return string[:bagIndex].strip(), int(bagCount)
        else: 
            return string[:bagIndex].strip()

    def __str__(self):
        return 'Bag color: {} contains {}'.format(self.Color, self.Contain)
        

def GetLines():
    file = open("day7/entries.txt")
    entries = file.readlines()
    for i in range(len(entries)):
        entries[i] = entries[i].rstrip()
    return entries

lines = GetLines()
myBagColor = 'shiny gold'

bags = list()

for line in lines:
    bag = Bag(line)
    bags.append(bag)
            
myBag = [x for x in bags if x.Color == myBagColor][0]
totalBags = myBag.GetContainBagCount(bags)

print(totalBags)
