def GetLines():
    with open("day18\\entries.txt") as f:
        entries = f.readlines()
    operations = list()
    for entry in entries:
        entry = entry.rstrip()
        entry = entry.replace('(', '( ')
        entry = entry.replace(')', ' )')
        operations.append(entry.split(' '))
    return operations

def ResolveOperation(operation, index = 0):
    result = 0
    operator = '+'
    while index < len(operation):
        element = operation[index]
        if element.isnumeric():
            element = int(element)
            result = MultiplyOrAdd(result, element, operator)
        elif element in ('+', '*'):
            operator = element
        elif element == '(':
            parentesis, index = ResolveOperation(operation, index + 1)
            result = MultiplyOrAdd(result, parentesis, operator)
        elif element == ')':
            return result, index
        else:
            print('{}: not recognized'.format(element))
        index += 1
    return result

def MultiplyOrAdd(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    else:
        result = num1 * num2
    #print('{} {} {} = {}'.format(num1, operator, num2, result))
    return result


if __name__ == "__main__":
    operations = GetLines()
    total = 0
    for operation in operations:
        result = ResolveOperation(operation)
        print('{} = {}'.format(' '.join(operation), result))
        total += result
        #print()
    print(total)
