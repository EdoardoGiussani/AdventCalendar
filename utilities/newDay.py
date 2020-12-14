from datetime import date
from pathlib import Path


if __name__ == "__main__":
    print('Select day for part two or leave blank for today:')
    day = input()
    if day == '':
        day = date.today().strftime('%d')
    name = 'day{}'.format(day)
    Path(name).mkdir(parents=True, exist_ok=True)

    lines = ('def GetLines():\n', 
             '    with open("{}\\\\entries.txt") as f:\n'.format(name),
             '        entries = f.readlines()\n'
             '    return entries\n\n\n',
             'if __name__ == "__main__":\n',
             '    entries = GetLines()\n')

    fileName = '{}\\{}.1.py'.format(name, name)
    if Path(fileName).is_file():
        print('{} already exists.\nPlease remove it if you want to create a new day.'.format(fileName))
        quit()

    with open (fileName, 'w') as f:
        f.writelines(lines)
    f = open('{}\\entries.txt'.format(name), 'w')
    f.close()

    print('Created {}'.format(name))