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
game.move({'from': 'A7', 'to': 'A6'})
game.move({'from': 'B2', 'to': 'B4'})
game.move({'from': 'B4', 'to': 'B5'})
game.move({'from': 'A6', 'to': 'B5'})
game.move({'from': 'A2', 'to': 'A4'})
# game.move({'from': 'A4', 'to': 'B5'})
game.move({'from': 'A8', 'to': 'A4'})
game.move({'from': 'E2', 'to': 'E4'})
game.move({'from': 'E4', 'to': 'E5'})
game.move({'from': 'E1', 'to': 'E2'})
game.move({'from': 'E2', 'to': 'E3'})
game.move({'from': 'E3', 'to': 'E4'})
# game.move({'from': 'D6', 'to': 'G6'})
# game.move({'from': 'C6', 'to': 'C4'})
# game.move({'from': 'C4', 'to': 'A4'})
# game.move({'from': 'A4', 'to': 'H4'})
printer.simple_print(game.board)
printer.info_print(game.board)

print(engine.simple_evaluate_board(game.board, game.w_pieces, game.b_pieces))

