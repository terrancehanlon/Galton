

class Mover:

    def __init__(self):
        pass

    # rank = row numbers
    def get_rank(self, location):
        return int(location[1])

    # file = column letters
    def get_file(self, location):
        return location[0]

    def get_rank_distance(self, info):
        return abs(self.get_rank(info['to']) - self.get_rank(info['from']))
        
    def check_next_file(self, info):
        if info['from'] == 'H':
            return -1
        print("info[to] is ", info['to'], "returning", chr(ord(self.get_file(info['from'])) + 1))
        return chr(ord(self.get_file(info['from'])) + 1)
    
    def check_prev_file(self, info):
        if info['from'] == 'A':
            return -1
        return chr(ord(self.get_file(info['from'])) - 1)

    ####### diag ##########
    def diag_right_positive(self, info, board, distance):
        #going positive
        z = 1
        j = 'A'
        for i in range(1, distance + 1):
            j = self.check_next_file(info)
            z = z+1
            if board[str(j) + str(z)] != 0:
                if i == distance:
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        #At last spot to check, and it's 
                        return True
                    else:
                        return False
                print("NOT VALID MOVE B")
                return False
        return True
    
    def diag_right_negative(self, info, board, distance):
        # going negative
        z = 1
        j = 'A'
        for i in range(1, distance + 1):
            j = self.check_next_file(info)
            z = z - 1
            if board[str(j) + str(z)] != 0:
                if i == distance:
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                    else:
                        return False
                print("not vald move b")
                return False
        return True

    def diag_left_positive(self, info, board, distance):
        z = 1
        j = 'A'
        for i in range(1, distance + 1):
            j = self.check_prev_file(info)
            z = z + 1
            if board[str(j) + str(z)] != 0:
                if i == distance:
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                    else:
                        return False
                print("NOT VALID MOVE B")
                return False
        return True

    def diag_left_negative(self, info, board, distance):
        z = 1
        j = 'A'
        for i in range(1, distance+1):
            j = self.check_prev_file(info)
            z = z - 1
            if board[str(j) + str(z)] != 0:
                if i == distance:
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                    else:
                        return False
                print("NOT VALID MOVE B")
                return False

    #### UP and Down ######

    def up_board(self, info, board):
        print("IP")
        j = self.get_file(info['from'])
        z = self.get_rank(info['from'])
        distance = abs( self.get_rank(info['from']) - self.get_rank(info['to']))
        for i in range(1, distance+1):
            z = z + 1
            if board[str(j) + str(z)] != 0:
                if i == distance:
                    print("AT END")
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        print("GOOD TAKES PIECE")
                        return True
                    else:
                        return False
                print("NOT VALID")
                return False
        print("VALID")
        return True

    def down_board(self, info, board):
        print("Down")
        j = self.get_file(info['from'])
        z = self.get_rank(info['from'])

        distance = abs( self.get_rank(info['from']) - self.get_rank(info['to']))
        print("distance:", distance)
        for i in range(1, distance + 1):
            z = z - 1
            if board[str(j) + str(z)] != 0:
                if i == distance:
                    print("AT END")
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        print("GOOD TAKES PIECE")
                        return True
                    else:
                        return False
                print("NOT VALID")
                return False
        print("VALID")
        return True

    def right_board(self, info, board):
        print("right")
        j = self.get_file(info['from'])
        z = self.get_rank(info['from'])
        x1 = ord(self.get_file(info['to']))
        x2 = ord(self.get_file(info['from']))
        for i in range(1, abs(x1-x2)+1):
            j = chr(ord(j) + 1)
            print("j:", j)
            if board[str(j) + str(z)] != 0:
                if i == abs(x1-x2):
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                    else:
                        return False
                return False
        return True

    def left_board(self, info, board):
        print("right")
        j = self.get_file(info['from'])
        z = self.get_rank(info['from'])
        x1 = ord(self.get_file(info['to']))
        x2 = ord(self.get_file(info['from']))
        for i in range(1, abs(x1-x2)+1):
            j = chr(ord(j) - 1)
            print("j:", j)
            if board[str(j) + str(z)] != 0:
                if i == abs(x1-x2):
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                    else:
                        return False
                return False
        return True

    ### knight
    def hook(self, info, board):
        print("hooking")
        # up 2 left 1
        # up 2 right 1
        # down 2 right 1
        # down 2 left 1
        # right 2 up 1
        # right 2 down 1
        # left 2 up 1
        # left 2 down 1

        # up 2 left 1
        x1 = self.get_file(info['from'])
        y1 = self.get_rank(info['from'])
        
        x2 = self.get_file(info['to'])
        y2 = self.get_rank(info['to'])


        # vertical hook
        if abs( y1 - y2) == 2:
            if abs(ord(x1) - ord(x2)) == 1:
                if board[info['to']] != 0:
                    if board[info['to']]['is_player'] == False:
                        return True
                else:
                    return True
        #horizontal hook
        if abs(ord(x1) - ord(x2)) == 2:
            if abs(y1 - y2) == 1:
                if board[info['to']] != 0:
                    if board[info['to']]['is_player'] == False:
                        return True
                else:
                    return True
        return False




