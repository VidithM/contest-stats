from standings import *

at = 0
columns = []
rows = []

with open('signups.tsv', 'r') as signups:
    for ln in signups:
        if(at == 0):
            columns = ln.split('\t')
        else:
            rows.append(ln.split('\t'))
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
    print('Required columns are not present in signups.tsv!')
    exit()

standings_by_year = {}
overall_standings = []
print(first_name_idx)
print(columns)
for participant in rows:
    first_name = participant[first_name_idx]
    last_name = participant[last_name_idx]
    handle = participant[handle_idx].lower()
    year = -1
    if('+' in participant[year_idx]):
        year = int(participant[year_idx][:-1])
    else:
        year = int(participant[year_idx])
    checked = participant[checked_idx]
    
    '''
    if(checked != 'yes'):
        continue
    '''

    if(valid_participant(handle)):
        overall_standings.append((get_rank(handle), handle))
        if(year in standings_by_year):
            standings_by_year[year].append((get_rank(handle), handle))
        else:
            standings_by_year[year] = [(get_rank(handle), handle)]
    else:
        print(f'Handle "{handle}" does not exist in standings!')

for elem in standings_by_year:
    standings_by_year[elem].sort()
    print(f'=== C/O {elem} STANDINGS: ===')
    for i in range(len(standings_by_year[elem])):
        print(f'{i + 1}: {standings_by_year[elem][i][1]}')

overall_standings.sort()
print('\n\n')
print('=== OVERALL STANDINGS: ===')
for i in range(len(overall_standings)):
    print(f'{i + 1}: {overall_standings[i][1]}')