# piece : {isPlayer: bool, type: str, square: str}
# square = {location: str, piece: piece}
# info : {type: str, location: str, is_player: bool}


class Engine:

    def evaluate_pieces(self, pieces1, pieces2):
        return 200 * (pieces1['K'] - pieces2['K']) + 9 * (pieces1['Q'] - pieces2['Q']) + 5 * (pieces1['R'] - pieces2['R']) + 3 * (pieces1['B'] - pieces2['B']) + 1 * (pieces1['P'] - pieces2['P'])

    def simple_evaluate_board(self, board, w_pieces, b_pieces):
        w_eval_dict = {}
        b_eval_dict = {}

        for w in w_pieces:
            if w['type'] in w_eval_dict:
                w_eval_dict[w['type']] = w_eval_dict[w['type']] + 1
            else:
                w_eval_dict[w['type']] = 1
            
        
        for b in b_pieces:
            if b['type'] in b_eval_dict:
                b_eval_dict[b['type']] = b_eval_dict[b['type']] + 1
            else:
                b_eval_dict[b['type']] = 1

        return {'white_score': 1 * self.evaluate_pieces(w_eval_dict, b_eval_dict), 'black_score': -1 * self.evaluate_pieces(w_eval_dict, b_eval_dict)}
        

    def minimax(self, board):
        print()
