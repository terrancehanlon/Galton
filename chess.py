
from mover import Mover

class Chess:
    def __init__(self):
        self.board = {}
        self.w_pieces = []
        self.b_pieces = []
        self.file_value = {}
        self.mover = Mover()
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
    
    
    # helper
    def get_rank_distance(self, info):
        return abs(self.get_rank(info['to']) - self.get_rank(info['from']))
    
    def check_next_file(self, info):
        if info['from'] == 'H':
            return -1
        # print("a:", chr(ord(self.get_file(info['from'])) + 1))
        # print(info)
        print("info[from] is ", info['from'], "Get file:", self.get_file(info['to']), "returning", chr(ord(self.get_file(info['from'])) + 1))
        return chr(ord(self.get_file(info['from'])) + 1)
    
    def check_prev_file(self, info):
        if info['from'] == 'A':
            return -1
        return chr(ord(self.get_file(info['from'])) - 1)
    
    def square_occupied(self, info):
        if self.board[info['to']] == 0:
            return False
        return True

    # info {from: str, to: str}
    def is_valid_move(self, info):
        p = self.board[info['from']]
        # Pawn
        if p['type'] == 'P':
            print("MOVING PAWN")
            # if p['is_player']:
            if self.get_rank_distance(info) == 1:
                #move forward 1 without taking
                if self.get_file(info['from']) == self.get_file(info['to']):
                    if not self.square_occupied(info):
                        print("VALID MOVE 1 up")
                        return True
                # move foward 1 (diag) to take
                # take to right
                elif self.check_next_file(info) == self.get_file(info['to']):
                    print("VALID MOVE ready to take")
                    if self.square_occupied(info) and not self.board[info['to']]['is_player']:
                        print("TAKING PIECE")
                        return True
                # take to left
                elif self.check_prev_file(info) == self.get_file(info['to']):
                    print("VALID MOVE READU TO TALE LEFT")
                    #bunch of extra useless checks?
                    if self.square_occupied(info) and self.board[info['to']]['is_player'] != self.board[info['from']]['is_player']:
                        print("TAKING PIECE")
                        return True
                    else:
                        return False


            elif self.get_rank_distance(info) == 2:
                #move forward 2 without taking
                if self.get_file(info['from']) == self.get_file(info['to']):
                    if self.board[info['to']] == 0:
                        print("VALID MOVE up 2")
                        return True
        
        if p['type'] == 'B':
            print("moving bishop")
            x2_minus_x1 = abs(ord(self.get_file(info['to'])) - ord(self.get_file(info['from'])))
            y2_minus_y1 = abs(self.get_rank(info['to']) - self.get_rank(info['from']))
            if x2_minus_x1 == y2_minus_y1:
                if chr(ord(self.get_file(info['to']))) < chr(ord(self.get_file(info['from']))):
                    # going to left
                    if self.get_rank(info['from']) < self.get_rank(info['to']):
                        # going positive
                        return self.mover.diag_left_positive(info, self.board, x2_minus_x1)
                    elif self.get_rank(info['from']) > self.get_rank(info['to']):
                        # going negative
                        return self.mover.diag_left_negative(info, self.board, x2_minus_x1)
                elif chr(ord(self.get_file(info['to']))) > chr(ord(self.get_file(info['from']))):
                    # going right
                    if self.get_rank(info['from']) < self.get_rank(info['to']):
                        return self.mover.diag_right_positive(info, self.board, x2_minus_x1)
                    elif self.get_rank(info['from']) > self.get_rank(info['to']):
                        # going negative
                        return self.mover.diag_right_negative(info, self.board,x2_minus_x1)
                return True
        if p['type'] == 'K':
            pass
        if p['type'] == 'Q':
            # move on same column
            if self.mover.get_file(info['to']) == self.mover.get_file(info['from']):
                #move up board
                if self.mover.get_rank(info['from']) < self.mover.get_rank(info['to']):
                    return self.mover.up_board(info, self.board)
                elif self.mover.get_rank(info['from']) > self.mover.get_rank(info['to']):
                    return self.mover.down_board(info, self.board)
            # move left or right
            elif self.mover.get_rank(info['to']) == self.mover.get_rank(info['from']):
                if ord(self.mover.get_file(info['from'])) < ord(self.mover.get_file(info['to'])):
                    return self.mover.up_board(info, self.board)
                elif ord(self.mover.get_file(info['from'])) > ord(self.mover.get_file(info['to'])):
                    return self.mover.down_board(info, self.board)
            else:
                x2_minus_x1 = abs(ord(self.get_file(info['to'])) - ord(self.get_file(info['from'])))
                y2_minus_y1 = abs(self.get_rank(info['to']) - self.get_rank(info['from']))
                if x2_minus_x1 == y2_minus_y1:
                    if chr(ord(self.get_file(info['to']))) < chr(ord(self.get_file(info['from']))):
                        # going to left
                        if self.get_rank(info['from']) < self.get_rank(info['to']):
                            # going positive
                            return self.mover.diag_left_positive(info, self.board, x2_minus_x1)
                        elif self.get_rank(info['from']) > self.get_rank(info['to']):
                            # going negative
                            return self.mover.diag_left_negative(info, self.board, x2_minus_x1)
                    elif chr(ord(self.get_file(info['to']))) > chr(ord(self.get_file(info['from']))):
                        # going right
                        if self.get_rank(info['from']) < self.get_rank(info['to']):
                            return self.mover.diag_right_positive(info, self.board, x2_minus_x1)
                        elif self.get_rank(info['from']) > self.get_rank(info['to']):
                            # going negative
                            return self.mover.diag_right_negative(info, self.board,x2_minus_x1)
                    return True
        if p['type'] == 'N':
             pass
        if p['type'] == 'R':
            print("moving rook")
            # Same file so same column
            if self.mover.get_file(info['from']) == self.mover.get_file(info['to']):
                if self.mover.get_rank(info['from']) < self.mover.get_rank(info['to']):
                    return self.mover.up_board(info, self.board)
                elif self.mover.get_rank(info['from']) > self.mover.get_rank(info['to']):
                    return self.mover.down_board(info, self.board)
            elif self.mover.get_rank(info['from']) == self.mover.get_rank(info['to']):
                print("rank from:", self.mover.get_rank(info['from']), "rank to:", self.mover.get_rank(info['to']))
                if ord(self.mover.get_file(info['from'])) < ord(self.mover.get_file(info['to'])):
                    return self.mover.right_board(info, self.board)
                elif ord(self.mover.get_file(info['from'])) > ord(self.mover.get_file(info['to'])):
                    return self.mover.left_board(info, self.board)

        print("NOT VALID MOVE")
        return False


    def init_pieces(self):
        self.init_pawns()
        self.init_rooks()
        self.init_bishops()
        self.init_knights()
        self.init_queens()
        self.init_kings()

    