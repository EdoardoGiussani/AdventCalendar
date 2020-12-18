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

def ResolveOperation(operation):
    for i in range(len(operation)):
        element = operation[i]
        if isinstance(element, list):
            operation[i] = ResolveOperation(element)

    while '+' in operation:    
        i = 0
        while i < len(operation):
            element = operation[i]
            if element == '+':
                num1 = operation[i - 1]
                num2 = operation[i + 1]
                operation[i + 1] = num1 + num2
                del operation[i - 1]
                del operation[i - 1]
            i += 1

    while '*' in operation: 
        i = 0
        while i < len(operation):
            element = operation[i]
            if element == '*':
                num1 = operation[i - 1]
                num2 = operation[i + 1]
                operation[i + 1] = num1 * num2
                del operation[i - 1]
                del operation[i - 1] 
            i += 1
    if len(operation) > 1:
        print(operation)
    return operation[0]

def ParseOperation(operation, index = 0):
    parsedOperation = list()
    while index < len(operation):
        element = operation[index]
        if element.isnumeric():
            element = int(element)
        elif element == '(':
            element, index = ParseOperation(operation, index + 1)
        elif element == ')':
            return parsedOperation, index
        parsedOperation.append(element)
        index += 1
    return parsedOperation

if __name__ == "__main__":
    operations = GetLines()
    total = 0
    for operation in operations:
        op = ParseOperation(operation)
        result = ResolveOperation(op)
        print('{} = {}'.format(' '.join(operation), result))
        total += result
        #print()
    print(total)
