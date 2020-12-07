class Bag:
    def __init__(self, description):
        bagDescription = description.split('contain')

        self.Color = self._getBagColor(bagDescription[0])
        self.ContainedBags = list()
        containedBags = bagDescription[1].split(',')
        for bag in containedBags:
            bag = bag.strip()
            self.ContainedBags.append(self._getBagColor(bag))


    def _getBagColor(self, string):
        if string[0].isdigit():
            countIndex = string.find(' ')
            string = string[countIndex:]
        bagIndex = string.find(' bag')
        return string[:bagIndex].strip()

    def __str__(self):
        return 'Bag color: {} contains {}'.format(self.Color, self.ContainedBags)
        

def GetLines():
    file = open("day7/entries.txt")
    entries = file.readlines()
    for i in range(len(entries)):
        entries[i] = entries[i].rstrip()
    return entries



lines = GetLines()
myBagColor = 'shiny gold'
bags = list()
containerBags = list()

for line in lines:
    bag = Bag(line)
    if myBagColor in bag.ContainedBags:
        containerBags.append(bag)
    else:
        bags.append(bag)

lastCount = 0
while lastCount != len(containerBags):
    lastCount = len(containerBags)
    for bag in bags:
        for color in bag.ContainedBags:
            matches = [x for x in containerBags if x.Color == color]
            if len(matches) > 0:
                bags.remove(bag)
                containerBags.append(bag)
                break

print('Bags:\n\n')
for bag in bags:
    print(bag)
print('\n\ncontainerBags:\n\n')
for bag in containerBags:
    print(bag)
print(len(containerBags))

