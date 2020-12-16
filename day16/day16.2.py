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

def ValidTickets(tickets, fields):
    validTickets = list()
    for ticket in tickets:
        if IsValidTicket(ticket, fields):
            validTickets.append(ticket)
    return validTickets

def IsValidTicket(ticket, fields):
    for value in ticket:
        if not IsValidValue(value, fields):
            return False
    return True

def IsValidValue(value, fields):
    for field in fields:
        if IsValidInField(value, fields[field]):
            return True
    return False

def IsValidInField(value, field):
    return field[0] <= value <= field[1] or field[2] <= value <= field[3]

def IsValidColumn(field, col, tickets):
    for ticket in tickets:
        if not IsValidInField(ticket[col], field):
            return False
    return True


def FindFieldPositions(field, tickets):
    validCols = list()
    for i in range(len(tickets[0])):
        if IsValidColumn(field, i, tickets):
            validCols.append(i)
    return validCols


if __name__ == "__main__":
    entries = GetLines()
    fields, myTicket, nearbyTickets = ParseInput(entries)
    nearbyTickets = ValidTickets(nearbyTickets, fields)

    for field in fields:
        validCols = FindFieldPositions(fields[field], nearbyTickets)
        fields[field] = validCols
        print('Field: {}, validColumns = {}'.format(field, validCols))

    assignedFields = list()
    assignedCols = list()
    while len(assignedFields) < len(fields):
        for field in fields:
            if len(fields[field]) == 1:
                col = fields[field][0]
                assignedFields.append((field, col))
                assignedCols.append(col)
                #fields.pop(field)
                for field in fields:
                    if col in fields[field]:
                        fields[field].remove(col)
    print(fields)
    print(assignedFields)

    product = 1
    for field in assignedFields:
        if field[0].startswith('departure'):
            product *= myTicket[field[1]]
            print('Field: {}, Column: {}, myTicket: {}'.format(field[0], field[1], myTicket[field[1]]))
    print(product)