'''
Parses Codeforces standings page
'''
import re
from bs4 import BeautifulSoup

participants = None
soup = None

def build_participants():
    global participants

    content = ''
    with open('standings.html', 'r', encoding='utf-8') as standings:
        content = standings.read()

    soup = BeautifulSoup(content, 'html.parser')

    all_tr = soup.find_all('tr', attrs={'participantid': True})
    participants = []

    search_attr = re.compile(r'^contestant-cell.*$')

    for i in range(len(all_tr)):
        td = None
        if(i % 2):
            td = all_tr[i].find('td', attrs={'class': search_attr})
        else:
            td = all_tr[i].find('td', attrs={'class': search_attr})
        
        # Check if they are unofficial, or virtual
        handle = td.text
        if('*' in handle or '#' in handle):
            continue
        
        # Valid participant, add to list
        participants.append(handle.strip().lower())

def get_participant(rank: int) -> str:
    if(participants == None):
        build_participants()

    return participants[rank - 1]

def get_rank(handle: str) -> int:
    if(participants == None):
        build_participants()
    
    return participants.index(handle)
    
def valid_participant(handle: str) -> bool:
    if(participants == None):
        build_participants()

    return handle in participants

def num_participants() -> int:
    if(participants == None):
        build_participants()
    
    return len(participants)
