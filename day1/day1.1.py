import time

def GetExpences():
    with open('day1\\expenseReport.txt', 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i])
    lines.sort()
    return lines

def FindExpences(entries):
    i = 0
    j = len(expences) - 1
    exSum = expences[i] + expences[j]
    while exSum != 2020:
        if exSum > 2020:
            j -= 1
        else:
            i += 1
        if j == i:
            quit('The combination of two expences were not found.\nPlease, entry a different Expence Report')
        exSum = expences[i] + expences[j]
    return expences[i], expences[j]
        

if __name__ == "__main__":
    startTime = time.time()
    expences = GetExpences()
    expence1, expence2 = FindExpences(expences)
    
    print('Expences: {}, {}'.format(expence1, expence2))
    print('Sum: {}, Product: {}'.format(expence1 + expence2, expence1 * expence2))
    print('Solved in {} s'.format(time.time() - startTime))