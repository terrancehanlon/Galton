from chess import Chess
from printer import Printer
from engine import Engine

game = Chess()
printer = Printer()
engine = Engine()

game.init_empty_board()
game.init_pieces()
# game.move({'from': 'B7', 'to': 'B5'})
# game.move({'from': 'B5', 'to': 'B4'})
game.move({'from': 'B2', 'to': 'B3'})
game.move({'from': 'C1', 'to': 'A3'})
game.move({'from': 'A3', 'to': 'D6'})
game.move({'from': 'C7', 'to': 'C6'})
game.move({'from': 'C6', 'to': 'C5'})
game.move({'from': 'D6', 'to': 'C5'})
# game.move({'from': 'A7', 'to': 'A6'})
printer.simple_print(game.board)
# printer.info_print(game.board)

print(engine.simple_evaluate_board(game.board, game.w_pieces, game.b_pieces))

