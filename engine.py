# piece : {isPlayer: bool, type: str, square: str}
# square = {location: str, piece: piece}
# info : {type: str, location: str, is_player: bool}

from termcolor import colored

board = {}
w_pieces = []
b_pieces = []

class Engine:

    

def insert_piece(info):
    board[info['location']] = {"type": info['type'], "is_player": info['is_player'], "location":  info['location']}


#print with location
def info_print():
    print()
    start_letter = 'A'
    start_number = 8
    tracker = 1

    for i in range(1, 65):
        if tracker > 8:
            tracker = 1
            start_letter = 'A'
            start_number = start_number - 1
            print()
        if board[start_letter + str(start_number)] != 0:
            print(start_letter + str(start_number), ":", board[start_letter + str(start_number)]['type'], " ", end='')
        else:
            print(start_letter + str(start_number), ":", board[start_letter + str(start_number)], " ", end='')
        start_letter = chr(ord(start_letter) + 1)
        tracker = tracker + 1
    print()


def simple_print():
    print()
    start_letter = 'A'
    start_number = 8
    tracker = 1

    for i in range(1, 65):
        if tracker > 8:
            tracker = 1
            start_letter = 'A'
            start_number = start_number - 1
            print()
        if board[start_letter + str(start_number)] != 0:
            if board[start_letter + str(start_number)]['is_player']:\
                print(colored(board[start_letter + str(start_number)]['type'], 'yellow'), " ", end='')
            else:
                print(colored(board[start_letter + str(start_number)]['type'], 'red'), " ", end='')
        else:
            print(board[start_letter + str(start_number)], " ", end='')
        start_letter = chr(ord(start_letter) + 1)
        tracker = tracker + 1
    print()

def w_pieces_print():
    for p in w_pieces:
        print(p)

def b_pieces_print():
    for p in b_pieces:
        print(p)

def init_empty_board():
    start_letter = 'A'
    start_number = 1

    for i in range(1, 65):
        if i <= 8:
            start_number = 1
        elif i <= 16:
            start_number = 2
        elif i <= 24:
            start_number = 3
        elif i <= 32:
            start_number = 4
        elif i <= 40:
            start_number = 5
        elif i <= 48:
            start_number = 6
        elif i <= 56:
            start_number = 7;
        elif i <= 64:
            start_number = 8
        if start_letter == 'I':
            start_letter = 'A'
        board[start_letter + str(start_number)] = 0
        start_number = start_number + 1
        start_letter = chr(ord(start_letter) + 1)

def init_pawns():
    start_letter = 'A'
    start_number = 2
    for i in range(1, 9):
        w_pieces.append({"type": "P", "is_player": True, "location": start_letter + str(start_number)})
        insert_piece({"type": "P", "is_player": True, "location": start_letter + str(start_number)})
        start_letter = chr(ord(start_letter ) + 1)
    
    start_letter = 'A'
    start_number = 7
    for i in range(1,9):
        b_pieces.append({"type": "P", "is_player": False, "location": start_letter + str(start_number)})
        insert_piece({"type": "P", "is_player": False, "location": start_letter + str(start_number)})
        start_letter = chr(ord(start_letter)+1)

def init_bishops():
    insert_piece({"type": "B", "is_player": True, "location": 'C1'})
    insert_piece({"type": "B", "is_player": True, "location": 'F1'})
    insert_piece({"type": "B", "is_player": False, "location": 'F8'})
    insert_piece({"type": "B", "is_player": False, "location": 'C8'})
    w_pieces.append({"type": "B", "is_player": True, "location": 'C1'})
    w_pieces.append({"type": "B", "is_player": True, "location": 'F1'})
    b_pieces.append({"type": "B", "is_player": False, "location": 'F8'})
    b_pieces.append({"type": "B", "is_player": False, "location": 'C8'})

def init_rooks():
    insert_piece({"type": "R", "is_player": True, "location": 'A1'})
    insert_piece({"type": "R", "is_player": True, "location": 'H1'})
    insert_piece({"type": "R", "is_player": False, "location": 'A8'})
    insert_piece({"type": "R", "is_player": False, "location": 'H8'})
    w_pieces.append({"type": "R", "is_player": True, "location": 'A1'})
    w_pieces.append({"type": "R", "is_player": True, "location": 'H1'})
    b_pieces.append({"type": "R", "is_player": False, "location": 'A8'})
    b_pieces.append({"type": "R", "is_player": False, "location": 'H8'})

def init_knights():
    insert_piece({"type": "N", "is_player": True, "location": 'B1'})
    insert_piece({"type": "N", "is_player": True, "location": 'G1'})
    insert_piece({"type": "N", "is_player": False, "location": 'B8'})
    insert_piece({"type": "N", "is_player": False, "location": 'G8'})
    w_pieces.append({"type": "N", "is_player": True, "location": 'B1'})
    w_pieces.append({"type": "N", "is_player": True, "location": 'G1'})
    b_pieces.append({"type": "N", "is_player": False, "location": 'B8'})
    b_pieces.append({"type": "N", "is_player": False, "location": 'G8'})

def init_queens():
    insert_piece({"type": "Q", "is_player": True, "location": 'D1'})
    insert_piece({"type": "Q", "is_player": False, "location": 'D8'})
    w_pieces.append({"type": "Q", "is_player": True, "location": 'D1'})
    b_pieces.append({"type": "Q", "is_player": False, "location": 'D8'})

def init_kings():
    insert_piece({"type": "K", "is_player": True, "location": 'E1'})
    insert_piece({"type": "K", "is_player": False, "location": 'E8'})
    w_pieces.append({"type": "K", "is_player": True, "location": 'E1'})
    b_pieces.append({"type": "K", "is_player": False, "location": 'E8'})

# info : {from: str, to: str}
def move(info):
    p = board[info['from']]
    board[info['from']] = 0
    board[info['to']] = p

    if p['is_player']:
        print("is player")
        for _p in w_pieces:
            if _p['location'] == info['from']:
                print('location is from')
                _p['location'] = info['to']


def init_pieces():
    init_pawns()
    init_rooks()
    init_bishops()
    init_knights()
    init_queens()
    init_kings()

init_empty_board()
init_pieces()

for i in w_pieces:
    print(i)

simple_print()
move({'from': 'A2', 'to': 'A4'})
simple_print()
info_print()

for i in w_pieces:
    print(i)


