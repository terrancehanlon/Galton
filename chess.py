

class Chess:
    def __init__(self):
        self.board = {}
        self.w_pieces = []
        self.b_pieces = []
        self.file_value = {}
        # self._value

    def insert_piece(self, info):
        self.board[info['location']] = {"type": info['type'], "is_player": info['is_player'], "location":  info['location']}

    def init_empty_board(self):
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
            self.board[start_letter + str(start_number)] = 0
            start_number = start_number + 1
            start_letter = chr(ord(start_letter) + 1)

    def init_pawns(self):
        start_letter = 'A'
        start_number = 2
        for i in range(1, 9):
            self.w_pieces.append({"type": "P", "is_player": True, "location": start_letter + str(start_number)})
            self.insert_piece({"type": "P", "is_player": True, "location": start_letter + str(start_number)})
            start_letter = chr(ord(start_letter ) + 1)
        
        start_letter = 'A'
        start_number = 7
        for i in range(1,9):
            self.b_pieces.append({"type": "P", "is_player": False, "location": start_letter + str(start_number)})
            self.insert_piece({"type": "P", "is_player": False, "location": start_letter + str(start_number)})
            start_letter = chr(ord(start_letter)+1)
    
    def init_bishops(self):
        self.insert_piece({"type": "B", "is_player": True, "location": 'C1'})
        self.insert_piece({"type": "B", "is_player": True, "location": 'F1'})
        self.insert_piece({"type": "B", "is_player": False, "location": 'F8'})
        self.insert_piece({"type": "B", "is_player": False, "location": 'C8'})
        self.w_pieces.append({"type": "B", "is_player": True, "location": 'C1'})
        self.w_pieces.append({"type": "B", "is_player": True, "location": 'F1'})
        self.b_pieces.append({"type": "B", "is_player": False, "location": 'F8'})
        self.b_pieces.append({"type": "B", "is_player": False, "location": 'C8'})

    def init_rooks(self):
        self.insert_piece({"type": "R", "is_player": True, "location": 'A1'})
        self.insert_piece({"type": "R", "is_player": True, "location": 'H1'})
        self.insert_piece({"type": "R", "is_player": False, "location": 'A8'})
        self.insert_piece({"type": "R", "is_player": False, "location": 'H8'})
        self.w_pieces.append({"type": "R", "is_player": True, "location": 'A1'})
        self.w_pieces.append({"type": "R", "is_player": True, "location": 'H1'})
        self.b_pieces.append({"type": "R", "is_player": False, "location": 'A8'})
        self.b_pieces.append({"type": "R", "is_player": False, "location": 'H8'})

    def init_knights(self):
        self.insert_piece({"type": "N", "is_player": True, "location": 'B1'})
        self.insert_piece({"type": "N", "is_player": True, "location": 'G1'})
        self.insert_piece({"type": "N", "is_player": False, "location": 'B8'})
        self.insert_piece({"type": "N", "is_player": False, "location": 'G8'})
        self.w_pieces.append({"type": "N", "is_player": True, "location": 'B1'})
        self.w_pieces.append({"type": "N", "is_player": True, "location": 'G1'})
        self.b_pieces.append({"type": "N", "is_player": False, "location": 'B8'})
        self.b_pieces.append({"type": "N", "is_player": False, "location": 'G8'})

    def init_queens(self):
        self.insert_piece({"type": "Q", "is_player": True, "location": 'D1'})
        self.insert_piece({"type": "Q", "is_player": False, "location": 'D8'})
        self.w_pieces.append({"type": "Q", "is_player": True, "location": 'D1'})
        self.b_pieces.append({"type": "Q", "is_player": False, "location": 'D8'})

    def init_kings(self):
        self.insert_piece({"type": "K", "is_player": True, "location": 'E1'})
        self.insert_piece({"type": "K", "is_player": False, "location": 'E8'})
        self.w_pieces.append({"type": "K", "is_player": True, "location": 'E1'})
        self.b_pieces.append({"type": "K", "is_player": False, "location": 'E8'})

    # rank = row numbers
    def get_rank(self, location):
        return int(location[1])

    # file = column letters
    def get_file(self, location):
        return location[0]

    # info : {from: str, to: str}
    def move(self,info):
        if self.is_valid_move(info) is False:
            return -1
        p = self.board[info['from']]
        self.board[info['from']] = 0
        self.board[info['to']] = p

        if p['is_player']:
            print("is player")
            for _p in self.w_pieces:
                if _p['location'] == info['from']:
                    print('location is from')
                    _p['location'] = info['to']
    
    # info {from: str, to: str}
    def is_valid_move(self, info):
        p = self.board[info['from']]
        # Pawn
        if p['type'] == 'P':
            if p['is_player']:
                if self.get_rank(info['to']) - self.get_rank(info['from']) == 1:
                    #move forward 1 without taking
                    if self.get_file(info['from']) == self.get_file(info['to']):
                        if self.board[info['to']] == 0:
                            print("VALID MOVE")
                            return True
                elif self.get_rank(info['to']) - self.get_rank(info['from']) == 2:
                    #move forward 2 without taking
                    if self.get_file(info['from']) == self.get_file(info['to']):
                        if self.board[info['to']] == 0:
                            print("VALID MOVE")
                            return True
            
        
        if ['type'] == 'K':
            pass
        if ['type'] == 'Q':
            pass
        if ['type'] == 'N':
            pass
        if ['type'] == 'R':
            pass
        if ['type'] == 'B':

            pass
        print("NOT VALID MOVE")
        return False


    def init_pieces(self):
        self.init_pawns()
        self.init_rooks()
        self.init_bishops()
        self.init_knights()
        self.init_queens()
        self.init_kings()

    