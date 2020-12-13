import time

def GetLines():
    file = open("day13/entries.txt")
    entries = file.readlines()
    return entries

def SchedulesToBuses(schedules):
    buses = list()
    for schedule in schedules:
        if schedule == 'x':
            continue
        bus = {}
        bus['cadency'] = int(schedule)
        bus['offset'] = schedules.index(schedule)
        bus['correction'] = 0
        while bus['offset'] > bus['cadency']:
            bus['offset'] -= bus['cadency']
            bus['correction'] += 1
        buses.append(bus)
    return buses

def FindFirstOccurrence(bus, firstBus, initialStep, step):
    cycles = initialStep
    result = False
    while result == False:
        result = ValidDeparture(bus, firstBus['cadency'] * cycles)
        if result == True:
            break
        else:
            cycles += step
    newInitialStep = cycles
    cycles += step
    result = False
    while result == False:
        result = ValidDeparture(bus, firstBus['cadency'] * cycles)
        if result == True:
            break
        else:
            cycles += step
    newStep = cycles - newInitialStep
    return newInitialStep, newStep           

def ValidDeparture(bus, time):
    nextDep = NextDeparture(bus['cadency'], time)
    if nextDep - time == bus['offset']:
        return True
    else: 
        return False
        
def NextDeparture(cadency, now):
    if now % cadency == 0:
        return now
    return (int(now / cadency) + 1) * cadency

startTime = time.time()
lines = GetLines()
schedule = lines[1].split(',')
buses = SchedulesToBuses(schedule)
print(buses)
#buses = sorted(buses, key=lambda k: k['cadency'])
#print(buses)
initialStep = 1
step = 1
for bus in buses[1:]:
    initialStep, step = FindFirstOccurrence(bus, buses[0], initialStep, step)
    print(bus, initialStep, step)

print(initialStep * buses[0]['cadency'])
print(time.time() - startTime)