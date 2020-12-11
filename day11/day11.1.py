def GetLines():
    file = open("day11/entries.txt")
    entries = file.readlines()
    for i in range(len(entries)):
        entries[i] = list(entries[i].rstrip())
    return entries

def PrintSeats(seats):
    for row in seats:
        string = ''
        for col in row:
            string += col
        print(string)
    print('\n')

def CopySeats(seats):
    seatsCopy = list()
    for row in seats:
        seatsCopy.append(row.copy())
    return seatsCopy
    

def OccupieSeat(seats, row, col):
    occupied = 0
    for r in (-1, 0, 1):
        myRow = row + r
        if not -1 < myRow < len(seats):
            continue
        for c in (-1, 0, 1):
            myCol = col + c
            if not -1 < myCol < len(seats[myRow]):
                continue
            if r != 0 or c != 0:
                if seats[myRow][myCol] == '#':
                    occupied = occupied + 1

    if occupied >= 5:
        return False
    if occupied == 0:
        return True
    else: 
        return None

def NextRound(seats):
    nextSeats = CopySeats(seats)
    for r in range(len(seats)):
        for c in range(len(seats[r])):
            if seats[r][c] != '.':
                occupie = OccupieSeat(seats, r, c)
                if occupie == None:
                    continue
                elif occupie == True and seats[r][c] != '#':
                    nextSeats[r][c] = '#'
                elif occupie == False and seats[r][c] != 'L':
                    nextSeats[r][c] = 'L'
    return nextSeats


seats = GetLines()
PrintSeats(seats)
newSeats = NextRound(seats)

while seats != newSeats:
    seats = newSeats
    newSeats = NextRound(seats)
    PrintSeats(newSeats)

occupied = 0
for r in seats:
    for c in r:
        if c == '#':
            occupied += 1

print(occupied)
