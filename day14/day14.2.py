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
    while len(bits) < 36:
        bits.insert(0, '0')
    return bits

def CorrectedValue(mask, mem):
    for i in range(len(mask)):
        if mask[i] != '0':
            mem[i] = mask[i]
    return mem

def BitsToInt(bits):
    bits = ''.join(bits)
    return int(bits, 2)

def SumPossibleValues(bits, index = 0):
    bits = bits.copy()
    addresses = list()
    while bits[index] != 'X':
        index += 1
        if index == 36:
            addresses.append(BitsToInt(bits))
            return addresses
    if bits[index] == 'X':
        bits[index] = '0'
        addresses += SumPossibleValues(bits, index)
        bits[index] = '1'
        addresses += SumPossibleValues(bits, index)
    return addresses
        

if __name__ == "__main__":
    entries = GetLines()
    masks = ConvertEntries(entries)
    memory = {}
    print(masks)
    for mask in masks:
        for mem in mask['mems']:
            bits = CorrectedValue(mask['mask'], NumToBits(int(mem[0])))
            addresses = SumPossibleValues(bits)
            for addres in addresses:
                memory[addres] = mem[1]

    memSum = 0
    for mem in memory:
        memSum += BitsToInt(memory[mem])
    print(memSum)