from chess import Chess
from printer import Printer

game = Chess()
printer = Printer()

game.init_empty_board()
game.init_pieces()
game.move({'from': 'A2', 'to': 'A4'})
printer.simple_print(game.board)
printer.info_print(game.board)

