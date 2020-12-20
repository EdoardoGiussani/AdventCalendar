def GetLines():
    with open("day19\\entries2.txt") as f:
        entries = f.readlines()
    rules = {}
    i = 0
    while entries[i] != '\n':
        entry = entries[i].split(': ')
        if '"' in entry[1]:
            rules[int(entry[0])] = entry[1][1]
        else:
            rules[int(entry[0])] = ParseRule(entry[1])
        i += 1
    messages = entries[i + 1:]
    for i in range(len(messages)):
        messages[i] = messages[i].strip()
    return rules, messages

def ParseRule(rule):
    rules = rule.strip().split('|')
    for i in range(len(rules)):
        indexes = rules[i].strip().split(' ')
        for j in range(len(indexes)):
            indexes[j] = int(indexes[j])
        rules[i] = indexes
    return rules

def SolveRule(message, messageIndex, rules, ruleIndex):
    rule = rules[ruleIndex]
    startingMessageIndex = messageIndex

    for subRule in rule:
        if subRule == 'a' or subRule == 'b':
            return subRule == message[messageIndex], messageIndex
                
        else:
            messageIndex = startingMessageIndex
            for index in subRule:
                valid, messageIndex = SolveRule(message, messageIndex, rules, index)
                messageIndex += 1
                if not valid:
                    break
                if messageIndex == len(message):
                    if subRule.index(index) + 1 == len(subRule):
                        break
                    else:
                        valid = False
                        break
            if valid:
                return True, messageIndex - 1
    return False, startingMessageIndex
    
def IsValidMessage(message, rules):
    valid, messageIndex = SolveRule(message, 0, rules, 0)
    return valid and messageIndex == len(message) - 1

if __name__ == "__main__":
    rules, messages = GetLines()
    validCount = 0
    for message in messages:
        if IsValidMessage(message, rules):
            print(message)
            validCount += 1
    print(validCount)