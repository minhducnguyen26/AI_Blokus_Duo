from rules import Rules
from search import Search

class Player:
    def __init__(self, player_id:int, board:list):
        self.player_id = player_id
        self.board = board

        self.rules = Rules()
        self.available_pieces = self.rules.get_all_pieces()
        self.board_columns = self.rules.board_columns.copy()
        self.board_rows = self.rules.board_rows.copy()

        self.start_positions = self.rules.start_positions.copy()
        self.placed_first_piece = False

        self.search = Search()

        self.used_pieces = []
        self.move_tried_count = 0
        self.game_over = False

    def update_from_percepts(self, percepts: list[list]):
        self.board = percepts[0]
        self.start_positions = percepts[1]

    def make_a_move(self, use_minimax=False) -> (int, str, str):
        # Send current data to the search class
        self.search.unpack_data(self.get_data_for_search())

        # Decide which piece to place where
        column, row, piece_shape = self.search.made_decision(use_minimax, placed_first_piece=self.placed_first_piece)

        if not self.placed_first_piece:
            start_position = {
                "column": column,
                "row": row
            }
            self.made_first_move(start_position)

        self.thought_about_making_move()

        # Return the move
        return column, row, piece_shape

    def get_data_for_search(self):
        data = {
            "state": {
                "player_id": self.player_id,
                "board": self.board,
                "start_positions": self.start_positions,
                "available_pieces": self.available_pieces,
                "board_columns": self.board_columns,
                "board_rows": self.board_rows,
            },
            "is_game_over": self.done(),
            "depth": 5,
        }
        return data

    def remove_piece(self, piece_shape: str):
        self.available_pieces.remove(piece_shape)

        # if there are no more pieces left, the game is over
        if len(self.available_pieces) == 0:
            self.game_over = True

    def made_valid_move(self, piece_shape: str):
        # Add the piece to the used pieces list
        self.used_pieces.append(piece_shape)

        # Remove the piece from the available pieces list
        self.remove_piece(piece_shape)

        # Reset the move tried count
        self.move_tried_count = 0

    def thought_about_making_move(self):
        self.move_tried_count += 1

        # If the times the player thought about making a move 
        # is greater than twice the amount of pieces left, then
        # => There are no more valid moves left 
        # and the game is over for this player
        if self.move_tried_count > len(self.available_pieces) * 2:
            self.game_over = True

    def made_first_move(self, start_position: dict):
        self.placed_first_piece = True
        # self.start_positions.remove(start_position)

    def done(self) -> bool:
        return self.game_over

    def get_score(self):
        point = 0

        for piece_shape in self.used_pieces:
            point += self.rules.get_piece_point(piece_shape)

        return point