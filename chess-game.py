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
game.move({'from': 'G1', 'to': 'F3'})
game.move({'from': 'F3', 'to': 'D4'})
game.move({'from': 'D4', 'to': 'E2'})
# game.move({'from': 'D4', 'to': 'E1'})
# game.move({'from': 'A3', 'to': 'D3'})
# game.move({'from': 'D3', 'to': 'F5'})
# game.move({'from': 'A3', 'to': 'H3'})
# game.move({'from': 'H3', 'to': 'D3'})
# game.move({'from': 'B7', 'to': 'A6'})
# game.move({'from': 'H7', 'to': 'H5'})
# game.move({'from': 'H8', 'to': 'H6'})
# game.move({'from': 'H6', 'to': 'D6'})
# game.move({'from': 'D6', 'to': 'G6'})
# game.move({'from': 'C6', 'to': 'C4'})
# game.move({'from': 'C4', 'to': 'A4'})
# game.move({'from': 'A4', 'to': 'H4'})
printer.simple_print(game.board)
# printer.info_print(game.board)

print(engine.simple_evaluate_board(game.board, game.w_pieces, game.b_pieces))

