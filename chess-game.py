from chess import Chess
from printer import Printer
from engine import Engine

game = Chess()
printer = Printer()
engine = Engine()

game.init_empty_board()
game.init_pieces()
game.move({'from': 'A2', 'to': 'A4'})
printer.simple_print(game.board)
printer.info_print(game.board)

print(engine.simple_evaluate_board(game.board, game.w_pieces, game.b_pieces))

