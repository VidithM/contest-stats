import sys
from standings import get_rank, valid_participant

out_file = None

if(len(sys.argv) > 1):
    assert(len(sys.argv) == 3)
    assert(sys.argv[1] == '-f')
    out_file = open(sys.argv[2], 'w')

def print_line(content: str):
    if(out_file == None):
        print(content)
    else:
        print(content, file=out_file)

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
degree_idx = -1
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
    elif('Degree Type' in columns[i]):
        degree_idx = i
    elif('Checked In' in columns[i]):
        checked_idx = i

if(first_name_idx == -1 or last_name_idx == -1 or handle_idx == -1 or year_idx == -1 or degree_idx == -1 or checked_idx == -1):
    print_line('Required columns are not present in signups.tsv!')
    exit()

checked_handles = {}
standings_by_year = {}
overall_standings = []

for participant in rows:
    first_name = participant[first_name_idx]
    last_name = participant[last_name_idx]
    handle = participant[handle_idx].lower()
    degree = participant[degree_idx]

    if(handle in checked_handles):
        continue
    checked_handles[handle] = True

    year = -1
    if('+' in participant[year_idx]):
        year = int(participant[year_idx][:-1])
    else:
        year = int(participant[year_idx])
    
    if(checked_idx >= len(participant)):
        continue
    
    checked = participant[checked_idx].strip()
    
    if(checked != 'yes'):
        continue

    if(valid_participant(handle)):
        overall_standings.append((get_rank(handle), handle, first_name, last_name))
        if(degree == 'Undergraduate'):
            if(year in standings_by_year):
                standings_by_year[year].append((get_rank(handle), handle, first_name, last_name))
            else:
                standings_by_year[year] = [(get_rank(handle), handle, first_name, last_name)]
        else:
            if(degree in standings_by_year):
                standings_by_year[degree].append((get_rank(handle), handle, first_name, last_name))
            else:
                standings_by_year[degree] = [(get_rank(handle), handle, first_name, last_name)]
    else:
        print_line(f'Handle "{handle}" does not exist in standings!')

if('Graduate' in standings_by_year):
    standings_by_year['Graduate'].sort()
    print_line('=== GRADUATE STANDINGS: ===')
    for i in range(len(standings_by_year['Graduate'])):
        tup = standings_by_year['Graduate'][i]
        print_line(f'{i + 1} ({tup[0] + 1}): {tup[1]}, {tup[2]} {tup[3]}')

if('PhD' in standings_by_year):
    standings_by_year['PhD'].sort()
    print_line('=== PHD STANDINGS: ===')
    for i in range(len(standings_by_year['PhD'])):
        tup = standings_by_year['PhD'][i]
        print_line(f'{i + 1} ({tup[0] + 1}): {tup[1]}, {tup[2]} {tup[3]}')

print_line('\n')

for elem in standings_by_year:
    if(elem == 'Graduate' or elem == 'PhD'):
        continue
    standings_by_year[elem].sort()
    print_line(f'=== C/O {elem} STANDINGS: ===')
    for i in range(len(standings_by_year[elem])):
        tup = standings_by_year[elem][i]
        print_line(f'{i + 1} ({tup[0] + 1}): {tup[1]}, {tup[2]} {tup[3]}')

overall_standings.sort()
print_line('\n\n')
print_line('=== OVERALL STANDINGS: ===')
for i in range(len(overall_standings)):
    tup = overall_standings[i]
    print_line(f'{i + 1} ({tup[0] + 1}): {tup[1]}, {tup[2]} {tup[3]}')