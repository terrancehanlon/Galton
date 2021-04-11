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
game.move({'from': 'D2', 'to': 'D4'})
game.move({'from': 'C1', 'to': 'D2'})
game.move({'from': 'D2', 'to': 'B4'})
game.move({'from': 'D7', 'to': 'D5'})
game.move({'from': 'C8', 'to': 'F5'})
game.move({'from': 'F5', 'to': 'G6'})
game.move({'from': 'G6', 'to': 'F5'})
# game.move({'from': 'D6', 'to': 'C5'})
# game.move({'from': 'A7', 'to': 'A6'})
printer.simple_print(game.board)
# printer.info_print(game.board)

print(engine.simple_evaluate_board(game.board, game.w_pieces, game.b_pieces))

