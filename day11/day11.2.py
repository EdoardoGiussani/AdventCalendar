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

def FindNextSeat(seats, row, col, rowOffset, colOffset):
    row = row + rowOffset
    col = col + colOffset
    if not IsValidPosition(seats, row, col):
        return None, None
    while seats[row][col] == '.':
        row = row + rowOffset
        col = col + colOffset
        if not IsValidPosition(seats, row, col):
            return None, None
    return row, col

def IsValidPosition(seats, row, col):
    if -1 < row < len(seats):
        if -1 < col < len(seats[row]):
            return True
    return False

def OccupieSeat(seats, row, col):
    occupied = 0
    for r in (-1, 0, 1):
        for c in (-1, 0, 1):
            if r != 0 or c != 0:
                myRow, myCol = FindNextSeat(seats, row, col, r, c)
                if myRow is None:
                    continue
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
#PrintSeats(seats)
newSeats = NextRound(seats)

while seats != newSeats:
    seats = newSeats
    newSeats = NextRound(seats)
    #PrintSeats(newSeats)

occupied = 0
for r in seats:
    for c in r:
        if c == '#':
            occupied += 1

print(occupied)
