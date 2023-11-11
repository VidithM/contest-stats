from standings import *

at = 0
columns = []
rows = []

with open('signups.csv', 'r') as signups:
    for ln in signups:
        if(at == 0):
            columns = ln.split(',')
        else:
            rows.append(ln.split(','))
        at += 1

first_name_idx = -1
last_name_idx = -1
handle_idx = -1
year_idx = -1
checked_idx = -1

for i in range(len(columns)):
    if('First Name' in columns[i]):
        first_name_idx = i
    elif('Last Name' in columns[i]):
        last_name_idx = i
    elif('Codeforces Handle' in columns[i]):
        handle_idx = i
    elif('Graduation Year' in columns[i]):
        year_idx = i
    elif('Checked In' in columns[i]):
        checked_idx = i

if(first_name_idx == -1 or last_name_idx == -1 or handle_idx == -1 or year_idx == -1):
    print('Required columns are not present in signups.csv!')
    exit()

standings_by_year = {}
overall_standings = []

for participant in rows:
    first_name = participant[first_name_idx]
    last_name = participant[last_name_idx]
    handle = participant[handle_idx]
    year = int(participant[year_idx])
    checked = participant

    if(valid_participant(handle)):
        if(year in standings_by_year):
            standings_by_year[year].append((get_rank(handle), handle))
        else:
            standings_by_year[year] = [(get_rank(hande), handle)]
    else:
        print('Handle ${handle} does not exist in standings!')

print(standings_by_year)