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
    k = 1
    j = len(expences) - 1
    exSum = expences[i] + expences[j] + expences[k]
    while exSum != 2020:
        if exSum > 2020:
            j -= 1
        else:
            k += 1
        if j == k:
            i += 1
            k = i + 1
            j = len(expences) - 1
            if j == k:
                quit('The combination of three expences were not found.\nPlease, entry a different Expence Report')
        exSum = expences[i] + expences[j] + expences[k]
    return expences[i], expences[j], expences[k]

if __name__ == "__main__":
    startTime = time.time()
    expences = GetExpences()
    expence1, expence2, expence3 = FindExpences(expences)

    print('Expences: {}, {}, {}'.format(expence1, expence2, expence3))
    print('Sum: {}, Product: {}'.format(expence1 + expence2 + expence3, expence1 * expence2 * expence3))
    print('Solved in {} s'.format(time.time() - startTime))