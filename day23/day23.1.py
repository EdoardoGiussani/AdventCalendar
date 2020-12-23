def StringToCups(cups_string):
    cups = list()
    for c in cups_string:
        cups.append(int(c))
    return cups

def RemoveCups(cups, current_cup):
    current_cup_pos = cups.index(current_cup)
    removed_cups = list()
    for _ in range(3):
        if current_cup_pos + 1 == len(cups):
            current_cup_pos = -1
        removed_cups.append(cups.pop(current_cup_pos + 1))
    return cups, removed_cups

def SelectDestinationCup(cups, current_cup):
    destination_cup = current_cup
    while True:
        destination_cup -= 1
        if destination_cup < min(cups):
            destination_cup = max(cups)
        if destination_cup in cups:
            break
    return destination_cup

def PlaceRemovedCups(cups, removed_cups, destination_cup):
    destination_cup_pos = cups.index(destination_cup)
    for i in range(3):
        cups.insert(destination_cup_pos + i + 1, removed_cups[i])
    return cups

def SelectNextCurrentCup(cups, current_cup):
    current_cup_pos = cups.index(current_cup)
    if current_cup_pos + 1 == len(cups):
        current_cup_pos = -1
    next_current_cup = cups[current_cup_pos + 1]
    return next_current_cup

def Move(cups, current_cup, move_num):
    print('-- move {} --\ncups: {}, current: {}'.format(move_num, cups, current_cup))
    cups, removed_cups = RemoveCups(cups, current_cup)
    print('pick up: {}'.format(removed_cups))
    destination_cup = SelectDestinationCup(cups, current_cup)
    print('destination: {}'.format(destination_cup))
    cups = PlaceRemovedCups(cups, removed_cups, destination_cup)
    current_cup = SelectNextCurrentCup(cups, current_cup)
    return cups, current_cup

def CupsToString(cups):
    cups_string = ''
    for cup in cups:
        cups_string += str(cup)
    cups_strings = cups_string.split('1')
    result = cups_strings[1] + cups_strings[0]
    return result

if __name__ == "__main__":
    cups = '916438275'  # My puzzle input
    # cups = '389125467'  # Example input
    cups = StringToCups(cups)
    current_cup = cups[0]
    for i in range(100):
        cups, current_cup = Move(cups, current_cup, i + 1)
    print(CupsToString(cups))




