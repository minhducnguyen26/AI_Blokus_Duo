from rules import Rules
from pieces import Pieces

class BlokusDuo:
    def __init__(self):
        self.rules = Rules()

        self.board_columns = self.rules.board_columns.copy()
        self.board_rows = self.rules.board_rows.copy()

        self.board = []
        self.build_board()

        self.pieces = Pieces(self.board)

        self.start_positions = self.rules.start_positions.copy()

    def build_board(self):
        for column in self.board_columns:
            row_dict = {}
            for row in self.board_rows:
                row_dict[row] = " "
            self.board.append(row_dict)

    def print_board(self):
        print()

        # Print the column numbers
        print("   ", end="")
        for column in self.board_columns:
            if column < 9:
                print(str(column) + ' ', end=" ")
            else:
                print(str(column), end=" ")
        print()

        # Print the rows
        for row in self.board_rows:
            print(row, end=" ")
            for column in self.board_columns:
                # 2 starting points of the game are in yellow
                for position in self.rules.start_positions:
                    if position["column"] == column and position["row"] == row:
                        print(
                            self.rules.get_yellow_string('[') 
                            + self.board[column][row] 
                            + self.rules.get_yellow_string(']'),
                            end="")
                        break

                else:
                    print("[" + self.board[column][row] + "]", end="")
            print()

    def get_observable_percepts(self) -> list[list]:
        return [self.board, self.start_positions]

    def apply_actions(self, column: int, row: str, piece_shape: str, player_id: int) -> bool:
        if not len(self.start_positions) == 0:
            # check if the piece is in the starting positions
            # if it is, remove it from the starting positions
            for position in self.start_positions:
                if position["column"] == column and position["row"] == row:
                    self.start_positions.remove(position)
                    break

        if not self.make_valid_move(column, row, piece_shape, player_id):
            return False

        # Update the board
        updated_board = self.pieces.board
        self.board = updated_board

        return True

    def make_valid_move(self, column:int, row:str, piece_shape:str, player_id: int) -> bool:
        if not self.pieces.place_piece(column, row, piece_shape, player_id):
            return False    
            
        return True

    def evaluate_game_result(self, player_1_score, player_2_score):
        result = None

        if player_1_score > player_2_score:
            result = "The winner is Player 1"
        elif player_2_score > player_1_score:
            result = "The winner is Player 2"
        else:
            result = "It's a draw"

        print()
        print("---------------- Game over! ----------------")
        print()
        print("The result is: " + result)

        self.print_board()