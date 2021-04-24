

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
        z = self.get_rank(info['from'])
        j = 'A'
        for i in range(1, distance + 1):
            j = self.check_next_file(info)
            z = z+1
            if board[str(j) + str(z)] != 0:
                if i == (distance) or str(j) + str(z) == info['to']:
                    print("is same ", str(j) + str(z))
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                    else:
                        print(str(j) + str(z), board[str(j) + str(z)])
                        print("NOT VALID MOVE B ested else here")
                        return False
            if board[str(j) + str(z)] != 0 and i < (distance + 1):
                print("falsing")
                return False
        return True
    
    def diag_right_negative(self, info, board, distance):
        # going negative
        z = self.get_rank(info['from'])
        j = self.get_file(info['from'])
        for i in range(1, distance + 1):
            j = chr(ord(j) + 1)
            z = z - 1
            if board[str(j) + str(z)] != 0:
                if i == (distance) or str(j) + str(z) == info['to']:
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                    else:
                        return False
                if board[str(j) + str(z)] != 0 and i < (distance + 1):
                    return False
        return True

    def diag_left_positive(self, info, board, distance):
        z = self.get_rank(info['from'])
        j = 'A'
        for i in range(1, distance + 1):
            j = self.check_prev_file(info)
            z = z + 1
            if board[str(j) + str(z)] != 0:
                if i == (distance) or str(j) + str(z) == info['to']:
                    print("is same ")
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                    else:
                        print(str(j) + str(z), board[str(j) + str(z)])
                        print("NOT VALID MOVE B ested else")
                        return False
            if board[str(j) + str(z)] != 0 and i < (distance + 1):
                print("falsing")
                return False
        return True

    def diag_left_negative(self, info, board, distance):
        z = self.get_rank(info['from'])
        j = 'A'
        for i in range(1, distance+1):
            j = self.check_prev_file(info)
            z = z - 1
            if board[str(j) + str(z)] != 0:
                if i == (distance) or str(j) + str(z) == info['to']:
                    print("is same ")
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                    else:
                        print(str(j) + str(z), board[str(j) + str(z)])
                        print("NOT VALID MOVE B ested else")
                        return False
            if board[str(j) + str(z)] != 0 and i < (distance + 1):
                print("falsing")
                return False
        return True

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
        for i in range(1, distance + 1):
            z = z - 1
            if board[str(j) + str(z)] != 0:
                if i == distance:
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                    else:
                        return False
                return False
        return True

    def right_board(self, info, board):
        j = self.get_file(info['from'])
        z = self.get_rank(info['from'])
        x1 = ord(self.get_file(info['to']))
        x2 = ord(self.get_file(info['from']))
        for i in range(1, abs(x1-x2)+1):
            j = chr(ord(j) + 1)
            if board[str(j) + str(z)] != 0:
                if i == abs(x1-x2):
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                    else:
                        return False
                return False
        return True

    def left_board(self, info, board):
        j = self.get_file(info['from'])
        z = self.get_rank(info['from'])
        x1 = ord(self.get_file(info['to']))
        x2 = ord(self.get_file(info['from']))
        for i in range(1, abs(x1-x2)+1):
            j = chr(ord(j) - 1)
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

    def get_all_attacked_positions(self, board, is_player):
        attacked_positions = {}
        
        for key in board:
            if board[key] == 0:
                continue
            elif board[key]['is_player'] == is_player:
                continue
            elif board[key]['type'] == 'R' and board[key]['is_player'] != is_player:
                start_file = self.get_file(board[key]['location'])
                start_rank = self.get_rank(board[key]['location'])
                #get attacked squares to right of rook
                attacked_square = chr(ord(start_file) + 1)
                while attacked_square != 'I':
                    if board[attacked_square + str(start_rank)] == 0:
                        if  attacked_square + str(start_rank) not in attacked_positions:
                            print("is attacked square", attacked_square + str(start_rank))
                            attacked_positions[attacked_square + str(start_rank)] = 1
                        attacked_square = chr(ord(attacked_square) + 1)
                    else:
                        break
                #get attacked squares to the left of hook
                attacked_square = self.get_file(board[key]['location'])
                attacked_square = chr(ord(start_file) - 1)
                while attacked_square >= 'A':
                    print(attacked_square + str(start_rank))
                    if board[attacked_square + str(start_rank)]  == 0:
                        if attacked_square + str(start_rank) not in attacked_positions:
                            attacked_positions[attacked_square + str(start_rank)] = 1
                        attacked_square = chr(ord(attacked_square) - 1)
                    else:
                        break
                #get attacked squares below rook
                attacked_square = self.get_file(board[key]['location'])
                attacked_square = chr(ord(start_file))
                attacked_rank = self.get_rank(board[key]['location']) - 1
                while attacked_rank > 0:
                    if board[attacked_square + str(attacked_rank)] == 0:
                        if attacked_square + str(attacked_rank) not in attacked_positions:
                            attacked_positions[attacked_square + str(attacked_rank)] = 1
                        attacked_rank = attacked_rank - 1
                    else:
                        break

                #get attacked squares above rook
                attacked_square = self.get_file(board[key]['location'])
                attacked_square = chr(ord(start_file))
                attacked_rank = self.get_rank(board[key]['location']) + 1
                while attacked_rank <= 8:
                    if board[attacked_square + str(attacked_rank)] == 0:
                        if attacked_square + str(attacked_rank) not in attacked_positions:
                            attacked_positions[attacked_square + str(attacked_rank)] = 1
                        attacked_rank = attacked_rank + 1
                    else:
                        break
            elif board[key]['type'] == 'B' and board[key]['is_player'] != 'B' and board[key]['is_player'] != is_player:
                #upper right diag
                attacked_square = chr(ord(self.get_file(board[key]['location'])) + 1)
                attacked_rank = self.get_rank(board[key]['location']) + 1
                while attacked_square != 'I' and attacked_rank <= 8 and attacked_rank > 0:
                    if board[attacked_square + str(attacked_rank)] == 0:
                        if attacked_square + str(attacked_rank) not in attacked_positions:
                            attacked_positions[attacked_square + str(attacked_rank)] = 1
                        attacked_rank = attacked_rank + 1
                        attacked_square = chr(ord(attacked_square) + 1)
                    else:
                        break
                # down right
                attacked_square = chr(ord(self.get_file(board[key]['location'])) + 1)
                attacked_rank = self.get_rank(board[key]['location']) - 1
                while attacked_square != 'I' and attacked_rank <= 8 and attacked_rank > 0:
                    if board[attacked_square + str(attacked_rank)] == 0:
                        if attacked_square + str(attacked_rank) not in attacked_positions:
                            attacked_positions[attacked_square + str(attacked_rank)] = 1
                        attacked_rank = attacked_rank - 1
                        attacked_square = chr(ord(attacked_square) + 1)
                    else:
                        break
                # up left
                attacked_square = chr(ord(self.get_file(board[key]['location'])) - 1)
                attacked_rank = self.get_rank(board[key]['location']) + 1
                while attacked_square >= 'A' and attacked_rank <= 8 and attacked_rank > 0:
                    if board[attacked_square + str(attacked_rank)] == 0:
                        if attacked_square + str(attacked_rank) not in attacked_positions:
                            attacked_positions[attacked_square + str(attacked_rank)] = 1
                        attacked_rank = attacked_rank + 1
                        attacked_square = chr(ord(attacked_square) - 1)
                    else:
                        break
                # down left
                attacked_square = chr(ord(self.get_file(board[key]['location'])) - 1)
                attacked_rank = self.get_rank(board[key]['location']) - 1
                while attacked_square >= 'A' and attacked_rank <= 8 and attacked_rank > 0:
                    if board[attacked_square + str(attacked_rank)] == 0:
                        if attacked_square + str(attacked_rank) not in attacked_positions:
                            attacked_positions[attacked_square + str(attacked_rank)] = 1
                        attacked_rank = attacked_rank + 1
                        attacked_square = chr(ord(attacked_square) - 1)
                    else:
                        break


                


        print(attacked_positions)
        return attacked_positions
                


    def king_can_move(self, info, board):
        print("moving king")
        attacked_positions = self.get_all_attacked_positions(board, board[info['from']]['is_player'])
        print(attacked_positions)
        if info['to'] not in attacked_positions:
            print("king can move")
            return True
        else:
            print("king cant move")
            return False
            





