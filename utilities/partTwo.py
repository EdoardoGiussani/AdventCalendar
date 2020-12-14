from datetime import date
from pathlib import Path

if __name__ == "__main__":
    print('Select day for part two or leave blank for today:')
    day = input()
    if day == '':
        day = date.today().strftime('%d')
    
    name1 = 'day{}\\day{}.1.py'.format(day, day)
    name2 = 'day{}\\day{}.2.py'.format(day, day)
    if not Path(name1).is_file():
        print('{} do not exists.\nPlease create day{} before continue.'.format(name1, day))
        quit()
    if Path(name2).is_file():
        print('{} already exists.\nPlease remove it if you want to create a new part two.'.format(name2))
        quit()
    with open(name1, 'r') as fr:
        content = fr.read()
    with open(name2, 'w') as fw:
        fw.write(content)

    print('Created part two for day{}'.format(day))
