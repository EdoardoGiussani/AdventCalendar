def GetLines():
    with open("day16\\entries.txt") as f:
        entries = f.readlines()
    return entries

def ParseInput(entries):
    index = 0
    fields = {}
    while entries[index] != '\n':
        infos = entries[index].split(': ')
        ranges = infos[1].split(' or ')
        range1 = ranges[0].split('-')
        range2 = ranges[1].split('-')
        ranges = (int(range1[0]), int(range1[1]), int(range2[0]), int(range2[1]))
        fields[infos[0]] = ranges
        index += 1

    index += 2
    myTicket = entries[index].split(',')
    for i in range(len(myTicket)):
        myTicket[i] = int(myTicket[i])

    index += 3
    nearbyTickets = list()
    while index < len(entries):
        nearTicket = entries[index].split(',')
        for i in range(len(nearTicket)):
            nearTicket[i] = int(nearTicket[i])
        nearbyTickets.append(nearTicket)
        index += 1
    return fields, myTicket, nearbyTickets

def IsValidValue(value, fields):
    for field in fields:
        if IsValidInField(value, fields[field]):
            return True
    return False

def IsValidInField(value, field):
    return field[0] <= value <= field[1] or field[2] <= value <= field[3]

if __name__ == "__main__":
    entries = GetLines()
    fields, myTicket, nearbyTickets = ParseInput(entries)

    invalidValues = 0
    for nearTicket in nearbyTickets:
        for value in nearTicket:
            if not IsValidValue(value, fields):
                invalidValues += value
                break
    
    print(invalidValues)

