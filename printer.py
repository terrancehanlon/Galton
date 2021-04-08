from termcolor import colored

class Printer:
    
    def info_print(self, board):
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

    def simple_print(self, board):
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

    def w_pieces_print(self, w_pieces):
        for p in w_pieces:
            print(p)

    def b_pieces_print(self, b_pieces):
        for p in b_pieces:
            print(p)