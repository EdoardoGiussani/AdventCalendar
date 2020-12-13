def GetLines():
    file = open("day13/entries.txt")
    entries = file.readlines()
    return entries

def NextDepartures(buses, now):
    times = list()
    for bus in buses:
        times.append(NextDeparture(bus, now))
    return times

def NextDeparture(bus, now):
    if bus == 'x':
        return 1000000000000
    bus = int(bus)
    return (int(now / bus) + 1) * bus

lines = GetLines()
now = int(lines[0])
buses = lines[1].split(',')

nextDeps = NextDepartures(buses, now)
nextDep = min(nextDeps)
bus = buses[nextDeps.index(nextDep)]
print((nextDep - now) * int(bus))