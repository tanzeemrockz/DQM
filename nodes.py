import os
def uinput(cmsg='DQM $> '):
    cleaned = input(cmsg).strip().lower()
    for char in ['?', '!', '.', ',']:
        cleaned = cleaned.replace(char, '')
    return cleaned

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')