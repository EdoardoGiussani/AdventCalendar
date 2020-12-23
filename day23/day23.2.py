def StringToCups(cups_string):
    cups = {}
    prev_cup = None
    for c in cups_string[::-1]:
        cups[int(c)] = prev_cup
        prev_cup = int(c)

    current_cup = prev_cup

    i = max(cups.keys()) + 1
    cups[int(cups_string[-1])] = i

    while i <= 1000000:
        cups[i] = i + 1
        i += 1
    cups[i - 1] = current_cup
    return cups, current_cup

def PrintCups(cups, current_cup):
    cups_string = str(current_cup)
    next_cup = cups[current_cup]
    while not next_cup == current_cup:
        cups_string += ' ' + str(next_cup)
        next_cup = cups[next_cup]
    return cups_string

def RemoveCups(cups, current_cup):
    removed_cups = list()
    removed_cup = cups[current_cup]
    for _ in range(3):
        removed_cups.append(removed_cup)
        removed_cup = cups[removed_cup]
    cups[current_cup] = removed_cup
    return cups, removed_cups

def SelectDestinationCup(cups, current_cup, removed_cups):
    destination_cup = current_cup
    while True:
        destination_cup -= 1
        if destination_cup < 1:
            destination_cup = len(cups)
        if destination_cup not in removed_cups:
            break
    return destination_cup

def PlaceRemovedCups(cups, removed_cups, destination_cup):
    cups[removed_cups[-1]] = cups[destination_cup]
    cups[destination_cup] = removed_cups[0]
    return cups

def SelectNextCurrentCup(cups, current_cup):
    next_current_cup = cups[current_cup]
    return next_current_cup

def Move(cups, current_cup, move_num):
    # print('-- move {} --\ncups: {}, current: {}'.format(move_num, PrintCups(cups, current_cup), current_cup))
    cups, removed_cups = RemoveCups(cups, current_cup)
    # print('pick up: {}'.format(removed_cups))
    destination_cup = SelectDestinationCup(cups, current_cup, removed_cups)
    # print('destination: {}'.format(destination_cup))
    cups = PlaceRemovedCups(cups, removed_cups, destination_cup)
    current_cup = SelectNextCurrentCup(cups, current_cup)
    return cups, current_cup

def CupsToString(cups):
    cups_string = ''
    next_cup = cups[1]
    while not next_cup == 1:
        cups_string += str(next_cup)
        next_cup = cups[next_cup]
    return cups_string

if __name__ == "__main__":
    cups = '916438275'  # My puzzle input
    # cups = '389125467'  # Example input
    cups, current_cup = StringToCups(cups)
    for i in range(10000000):
        cups, current_cup = Move(cups, current_cup, i + 1)
    first_number = cups[1]
    second_number = cups[first_number]
    print('{} * {} = {}'.format(first_number, second_number, first_number * second_number))
