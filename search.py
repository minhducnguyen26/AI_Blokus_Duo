import random
from pieces import Pieces

N_INFINITY = -1000000
P_INFINITY = 1000000

# interface "state" {
#     "player_id": int,
#     "board": list,
#     "start_positions": list[dict] (where dict = {column: int, row: str}),
#     "available_pieces": list,
#     "board_columns": list[int],
#     "board_rows": list[str],
# }

class Search:
    def __init__(self):
        self.pieces = None

        self.state = {} # see interface "state" above
        self.is_game_over = False
        self.depth = 0
        self.alpha = N_INFINITY
        self.beta = P_INFINITY

    def unpack_data(self, data: dict):
        self.state = data["state"]
        self.is_game_over = data["is_game_over"]
        self.depth = data["depth"]

        self.pieces = Pieces(self.state["board"])

    def made_decision(self, use_minimax: bool, placed_first_piece: bool) -> (int, str, str):
        if use_minimax:
            return self.make_intelligent_decision(placed_first_piece)
        else:
            return self.make_random_decision(placed_first_piece)

    def make_random_decision(self, placed_first_piece: bool) -> (int, str, str):
        random_column = 0
        random_row = ''

        if not placed_first_piece:
            random_start_position = random.choice(self.state["start_positions"])
            random_column = random_start_position["column"]
            random_row = random_start_position["row"]
        else:
            random_column = random.choice(self.state["board_columns"])
            random_row = random.choice(self.state["board_rows"])
        
        random_piece = random.choice(self.state["available_pieces"])
        
        return random_column, random_row, random_piece

    def make_intelligent_decision(self, placed_first_piece: bool) -> (int, str, str):
        best_score = N_INFINITY
        best_column = 0
        best_row = ''
        best_piece = 'o'

        player_id = self.state["player_id"]

        if not placed_first_piece:
            for position in self.state["start_positions"]:
                column = position["column"]
                row = position["row"]

                for piece_shape in self.state["available_pieces"]:
                    # Make a move
                    if not self.pieces.place_piece(column, row, piece_shape, player_id):
                        continue
                    # Evaluate the move
                    evaluation = self.minimax_for_start_position(self.state, self.is_game_over, self.depth, self.alpha, self.beta, False)
                    # Undo the move
                    self.pieces.remove_piece(column, row, piece_shape, player_id)
                    # Update best_score
                    if evaluation > best_score:
                        best_score = evaluation
                        best_column = column
                        best_row = row
                        best_piece = piece_shape
        else:
            for column in self.state["board_columns"]:
                for row in self.state["board_rows"]:
                    for piece_shape in self.state["available_pieces"]:
                        # Make a move
                        if not self.pieces.place_piece(column, row, piece_shape, player_id):
                            continue
                        # Evaluate the move
                        evaluation = self.minimax(self.state, self.is_game_over, self.depth, self.alpha, self.beta, False)
                        # Undo the move
                        self.pieces.remove_piece(column, row, piece_shape, player_id)
                        # Update best_score
                        if evaluation > best_score:
                            best_score = evaluation
                            best_column = column
                            best_row = row
                            best_piece = piece_shape

        return best_column, best_row, best_piece

    def evaluate_game_result(self):
        return 0

    def minimax(self, state: dict, is_game_over: bool, depth: int, alpha: int, beta: int, is_maximizing: bool) -> int:
        if depth == 0 or is_game_over:
            return self.evaluate_game_result()

        player_id = self.state["player_id"]

        if is_maximizing:
            max_eval = N_INFINITY
            for column in state["board_columns"]:
                for row in state["board_rows"]:
                    for piece_shape in state["available_pieces"]:
                        # Make a move
                        if not self.pieces.place_piece(column, row, piece_shape, player_id):
                            continue
                        # Evaluate the move
                        evaluation = self.minimax(state, is_game_over, depth - 1, alpha, beta, False)
                        # Undo the move
                        self.pieces.remove_piece(column, row, piece_shape, player_id)
                        # Update max_eval
                        max_eval = max(max_eval, evaluation)
                        # Update alpha
                        alpha = max(alpha, evaluation)
                        # Prune
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = P_INFINITY
            for column in state["board_columns"]:
                for row in state["board_rows"]:
                    for piece_shape in state["available_pieces"]:
                        # Make a move
                        if not self.pieces.place_piece(column, row, piece_shape, player_id):
                            continue
                        # Evaluate the move
                        evaluation = self.minimax(state, is_game_over, depth - 1, alpha, beta, True)
                        # Undo the move
                        self.pieces.remove_piece(column, row, piece_shape, player_id)
                        # Update min_eval
                        min_eval = min(min_eval, evaluation)
                        # Update beta
                        beta = min(beta, evaluation)
                        # Prune
                        if beta <= alpha:
                            break
            return min_eval

    def minimax_for_start_position(self, state: dict, is_game_over: bool, depth: int, alpha: int, beta: int, is_maximizing: bool) -> int:
        if depth == 0 or is_game_over:
            return self.evaluate_game_result()

        player_id = self.state["player_id"]

        if is_maximizing:
            max_eval = N_INFINITY
            for position in state["start_positions"]:
                column = position["column"]
                row = position["row"]

                for piece_shape in state["available_pieces"]:
                    # Make a move
                    if not self.pieces.place_piece(column, row, piece_shape, player_id):
                        continue
                    # Evaluate the move
                    evaluation = self.minimax_for_start_position(state, is_game_over, depth - 1, alpha, beta, False)
                    # Undo the move
                    self.pieces.remove_piece(column, row, piece_shape, player_id)
                    # Update max_eval
                    max_eval = max(max_eval, evaluation)
                    # Update alpha
                    alpha = max(alpha, evaluation)
                    # Prune
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = P_INFINITY
            for position in state["start_positions"]:
                column = position["column"]
                row = position["row"]

                for piece_shape in state["available_pieces"]:
                    # Make a move
                    if not self.pieces.place_piece(column, row, piece_shape, player_id):
                        continue
                    # Evaluate the move
                    evaluation = self.minimax_for_start_position(state, is_game_over, depth - 1, alpha, beta, True)
                    # Undo the move
                    self.pieces.remove_piece(column, row, piece_shape, player_id)
                    # Update min_eval
                    min_eval = min(min_eval, evaluation)
                    # Update beta
                    beta = min(beta, evaluation)
                    # Prune
                    if beta <= alpha:
                        break
            return min_eval