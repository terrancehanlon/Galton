

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
        if self.get_rank(info['from']) < self.get_rank(info['to']):
            #going positive
            z = 1
            j = 'A'
            for i in range(1, distance + 1):
                j = self.check_next_file(info)
                z = self.get_rank(info['from']) + 1
                if board[str(j) + str(z)] != 0:
                    if i == distance:
                        if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                            #At last spot to check, and it's 
                            return True
                    print("NOT VALID MOVE B")
                    return False
    
    def diag_right_negative(self, info, board, distance):
        # going negative
        z = 1
        j = 'A'
        for i in range(1, distance + 1):
            j = self.check_next_file(info)
            z = self.get_rank(info['from']) - 1
            if board[str(j) + str(z)] != 0:
                if i == distance:
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                print("not vald move b")
                return False

    def diag_left_positive(self, info, board, distance):
        z = 1
        j = 'A'
        for i in range(1, distance + 1):
            j = self.check_prev_file(info)
            z = self.get_rank(info['from']) + 1
            if board[str(j) + str(z)] != 0:
                if i == distance:
                    if board[str(j) + str(z)]['is_player'] != board[info['from']]['is_player']:
                        return True
                print("NOT VALID MOVE B")
                return False

    def diag_left_negative(self, info, board, distance):
        z = 1
        j = 'A'
        for i in range(1, distance+1):
            j = self.check_prev_file(info)
            z = self.get_rank(info['from']) - 1
            if board[str(j) + str(z)] != 0:
                if i == distance:
                    if board[str(j) + str(z)]['is_player'] != board[info['from']['is_player']]:
                        return True
                print("NOT VALID MOVE B")
                return False
