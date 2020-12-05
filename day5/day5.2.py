def GetLines():
    file = open("day5/entries.txt")
    entries = file.readlines()
    for i in range(len(entries)):
        entries[i] = entries[i].rstrip()
    return entries

def GetPosition(positions, rng):
    letters = list(positions)
    for letter in letters:
        rngs = SplitRange(rng)
        if letter == 'F' or letter == 'L':
            rng = rngs[0]
        else: 
            rng = rngs[1]
    return rng[0]

def SplitRange(rng):
    diff = rng[1] - rng[0]
    hDiff = diff//2
    lRng = [rng[0], rng[0]+hDiff]
    uRng = [rng[1] - hDiff, rng[1]]
    return [lRng, uRng]

lines = GetLines()
ids = list()
for line in lines:
    row = GetPosition(line[:7], [0, 127])
    col = GetPosition(line[7:], [0,7])
    seatId = row * 8 + col
    ids.append(seatId)
    #print('Col: {}; Row: {}'.format(col,row))

ids.sort()
print(ids)
for i in range(min(ids), max(ids)):
    if i not in ids:
        if i - 1 in ids and i + 1 in ids:
            print('Possible Id:', i) 