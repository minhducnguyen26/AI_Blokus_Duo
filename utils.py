from rules import Rules

class Utils:
    def __init__(self, board: list):
        self.rules = Rules()

        self.board_rows = self.rules.board_rows.copy()
        self.board_columns = self.rules.board_columns.copy()
        self.board = board

    #! Helper functions to get the rows/columns surrounding a piece
    def get_right_column(self, column: int) -> int:
        return self.board_columns[self.board_columns.index(column) + 1]

    def get_2_right_columns(self, column: int) -> int:
        return self.board_columns[self.board_columns.index(column) + 2]

    def get_left_column(self, column: int) -> int:
        return self.board_columns[self.board_columns.index(column) - 1]

    def get_row_below(self, row: str) -> str:
        return self.board_rows[self.board_rows.index(row) + 1]

    def get_row_above(self, row: str) -> str:
        return self.board_rows[self.board_rows.index(row) - 1]

    def get_2_rows_below(self, row: str) -> str:
        return self.board_rows[self.board_rows.index(row) + 2]

    def get_3_rows_below(self, row: str) -> str:
        return self.board_rows[self.board_rows.index(row) + 3]

    def get_4_rows_below(self, row: str) -> str:
        return self.board_rows[self.board_rows.index(row) + 4]

    #! Validation
    #* Basic validation
    def handle_basic_validation(self, column:int, row:str, piece_shape:str, player_id: int) -> bool:
        # Check if the piece is in the available pieces
        if piece_shape not in self.rules.get_all_pieces():
            print('Invalid piece')
            return False

        # Check if the piece is in the board
        if row not in self.board_rows or column not in self.board_columns:
            return False

        # Check if the piece is in a valid position
        if self.board[column][row] != ' ':
            return False

        return True

    #* Validate a piece's position before placing it
    def is_a_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        # Check above only if the piece is not on the top row
        if row != 'A':
            if self.board[column][self.get_row_above(row)] == self.rules.get_colored_string_from_player_id(player_id):
                return False
            
        # Check left only if the piece is not on the leftmost column
        if column != 0:
            if self.board[self.get_left_column(column)][row] == self.rules.get_colored_string_from_player_id(player_id):
                return False

        # Check right only if the piece is not on the rightmost column
        if column != 13:
            if self.board[self.get_right_column(column)][row] == self.rules.get_colored_string_from_player_id(player_id):
                return False

        # Check below only if the piece is not on the bottom row
        if row != 'N':
            if self.board[column][self.get_row_below(row)] == self.rules.get_colored_string_from_player_id(player_id):
                return False

        return True

    def is_i_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row == 'N':
            return False
        
        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        return True

    def is_l1_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'M':
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        return True

    def is_L1_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row == 'N' or column == 13:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_row_below(row), player_id):
            return False

        return True

    def is_l2_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'L':
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_3_rows_below(row), player_id):
            return False

        return True

    def is_L2_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'M' or column == 13:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_2_rows_below(row), player_id):
            return False

        return True

    def is_t_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'M' or column == 0:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_left_column(column), self.get_row_below(row), player_id):
            return False

        return True

    def is_O_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row == 'N' or column == 13:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), row, player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_row_below(row), player_id):
            return False

        return True

    def is_z_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row == 'N' or column >= 12:
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), row, player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_2_right_columns(column), self.get_row_below(row), player_id):
            return False

        return True

    def is_l3_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'K':
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_3_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_4_rows_below(row), player_id):
            return False

        return True

    def is_L3_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'L' or column == 13:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_3_rows_below(row), player_id):
            return False
        
        if not self.is_a_piece_valid(self.get_right_column(column), self.get_3_rows_below(row), player_id):
            return False

        return True

    def is_4_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'L' or column == 13:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False
        
        if not self.is_a_piece_valid(self.get_right_column(column), self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_3_rows_below(row), player_id):
            return False

        return True

    def is_6_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'M' or column == 0:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_left_column(column), self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_left_column(column), self.get_2_rows_below(row), player_id):
            return False

        return True

    def is_C_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'M' or column == 13:
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), row, player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        return True

    def is_t2_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'L' or column == 13:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_3_rows_below(row), player_id):
            return False

        return True

    def is_T_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'M' or column == 0 or column == 13:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_left_column(column), self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_2_rows_below(row), player_id):
            return False

        return True

    def is_L4_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'M' or column >= 12:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_2_right_columns(column), self.get_2_rows_below(row), player_id):
            return False

        return True

    def is_3_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'M' or column >= 12:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_2_rows_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_2_right_columns(column), self.get_2_rows_below(row), player_id):
            return False

        return True

    def is_4s_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'M' or column >= 12:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_2_right_columns(column), self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_2_right_columns(column), self.get_2_rows_below(row), player_id):
            return False

        return True

    def is_7_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'M' or column == 0 or column == 13:
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), row, player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_left_column(column), self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        return True

    def is_plus_shape_piece_valid(self, column: int, row: str, player_id: int) -> bool:
        if row >= 'M' or column == 0 or column == 13:
            return False

        if not self.is_a_piece_valid(column, self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_right_column(column), self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(self.get_left_column(column), self.get_row_below(row), player_id):
            return False

        if not self.is_a_piece_valid(column, self.get_2_rows_below(row), player_id):
            return False

        return True