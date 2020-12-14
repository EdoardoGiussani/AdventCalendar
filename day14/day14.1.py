def GetLines():
    with open("day14\\entries.txt") as f:
        entries = f.readlines()
    return entries

def ConvertEntries(entries):
    masks = list()
    mask = {}
    for entry in entries:
        if entry.startswith('mask ='):
            masks.append(mask)
            mask = {}
            mask['mask'] = list(entry[7:].rstrip())
            mask['mems'] = list()
        else:
            startPos = entry.find('[') + 1
            endPos = entry.find(']')
            pos = entry[startPos:endPos]
            val = NumToBits(int(entry[endPos + 4:]))
            mask['mems'].append((pos, val))
    masks.append(mask)
    return masks[1:]

def NumToBits(num):
    binary = bin(num)[2:]
    bits = list(binary)
    # for bit in binary:
    #     if bit == '1':
    #         bits.append(1)
    #     else:
    #         bits.append(0)
    while len(bits) < 36:
        bits.insert(0, '0')
    return bits

def CorrectedValue(mask, mem):
    for i in range(len(mask)):
        if mask[i] != 'X':
            mem[i] = mask[i]
    return mem

def BitsToInt(bits):
    bits = ''.join(bits)
    return int(bits, 2)

if __name__ == "__main__":
    entries = GetLines()
    masks = ConvertEntries(entries)
    memory = {}
    for mask in masks:
        for mem in mask['mems']:
            memory[mem[0]] = CorrectedValue(mask['mask'], mem[1])
            print( memory[mem[0]])

    memSum = 0
    for mem in memory:
        memSum += BitsToInt(memory[mem])
    print(memSum)