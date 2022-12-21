from rules import Rules
from utils import Utils

class Pieces:
    def __init__(self, board:list):
        self.rules = Rules()
        self.utils = Utils(board)

        self.board_rows = self.rules.board_rows.copy()
        self.board_columns = self.rules.board_columns.copy()
        self.board = board

    def get_piece_color(self, player_id:int):
        piece = ''
        if player_id == 1:
            piece = self.rules.player_1_piece
        elif player_id == 2:
            piece = self.rules.player_2_piece
        else:
            print('Invalid player')
        return piece

    def place_piece(self, column:int, row:str, piece_shape:str, player_id:int, is_remove_piece=False) -> bool:
        # This function places the piece in the board
        # and it will return whether the move is valid
        if not self.utils.handle_basic_validation(column, row, piece_shape, player_id):
            return False

        # Check if the first piece is valid
        if not self.utils.is_a_piece_valid(column, row, player_id):
            return False

        piece = ""
        if not is_remove_piece:
            piece = self.get_piece_color(player_id)

        #? All 'go' actions is from the perspective of the first piece placed

        #! 1 square
        # x
        if (piece_shape == 'o'):
            self.board[column][row] = piece
            return True
            
        #! 2 squares
        # x 
        # x
        elif (piece_shape == 'i'):
            if not self.utils.is_i_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            return True

        #! 3 squares
        # x 
        # x
        # x
        elif (piece_shape == 'l1'):
            if not self.utils.is_l1_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            return True

        # x 
        # x x
        elif (piece_shape == 'L1'):
            if not self.utils.is_L1_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go right 1 and down 1
            self.board[self.utils.get_right_column(column)][self.utils.get_row_below(row)] = piece
            return True

        #! 4 squares
        # x 
        # x
        # x
        # x
        elif (piece_shape == 'l2'):
            if not self.utils.is_l2_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            # go down 3
            self.board[column][self.utils.get_3_rows_below(row)] = piece
            return True

        # x 
        # x
        # x x
        elif (piece_shape == 'L2'):
            if not self.utils.is_L2_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            # go right 1 and down 2
            self.board[self.utils.get_right_column(column)][self.utils.get_2_rows_below(row)] = piece
            return True

        #   x 
        # x x 
        #   x 
        elif (piece_shape == 't'):
            if not self.utils.is_t_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            # go left 1 and down 1
            self.board[self.utils.get_left_column(column)][self.utils.get_row_below(row)] = piece
            return True

        # x x
        # x x
        elif (piece_shape == 'O'):
            if not self.utils.is_O_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go right 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go down 1
            self.board[self.utils.get_right_column(column)][row] = piece
            # go right 1 and down 1
            self.board[self.utils.get_right_column(column)][self.utils.get_row_below(row)] = piece
            return True

        # x x
        #   x x
        elif (piece_shape == 'z'):
            if not self.utils.is_z_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go right 1 
            self.board[self.utils.get_right_column(column)][row] = piece
            # go right 1 and down 1
            self.board[self.utils.get_right_column(column)][self.utils.get_row_below(row)] = piece
            # go right 2 and down 1
            self.board[self.utils.get_2_right_columns(column)][self.utils.get_row_below(row)] = piece
            return True

        #! 5 squares
        # x 
        # x
        # x
        # x
        # x
        elif (piece_shape == 'l3'):
            if not self.utils.is_l3_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            # go down 3
            self.board[column][self.utils.get_3_rows_below(row)] = piece
            # go down 4
            self.board[column][self.utils.get_4_rows_below(row)] = piece
            return True

        # x 
        # x
        # x
        # x x
        elif (piece_shape == 'L3'):
            if not self.utils.is_L3_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            # go down 3
            self.board[column][self.utils.get_3_rows_below(row)] = piece
            # go right 1 and down 3
            self.board[self.utils.get_right_column(column)][self.utils.get_3_rows_below(row)] = piece
            return True

        # x 
        # x
        # x x
        #   x
        elif (piece_shape == '4'):
            if not self.utils.is_4_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            # go right 1 and down 2
            self.board[self.utils.get_right_column(column)][self.utils.get_2_rows_below(row)] = piece
            # go right 1 and down 3
            self.board[self.utils.get_right_column(column)][self.utils.get_3_rows_below(row)] = piece
            return True

        #   x   
        # x x
        # x x
        elif (piece_shape == '6'):
            if not self.utils.is_6_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            # go left 1 and down 1
            self.board[self.utils.get_left_column(column)][self.utils.get_row_below(row)] = piece
            # go left 1 and down 2
            self.board[self.utils.get_left_column(column)][self.utils.get_2_rows_below(row)] = piece
            return True

        # x x   
        #   x
        # x x
        elif (piece_shape == 'C'):
            if not self.utils.is_C_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go right 1
            self.board[self.utils.get_right_column(column)][row] = piece
            # go right 1 and down 1
            self.board[self.utils.get_right_column(column)][self.utils.get_row_below(row)] = piece
            # go right 1 and down 2
            self.board[self.utils.get_right_column(column)][self.utils.get_2_rows_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            return True

        # x
        # x 
        # x x
        # x
        elif (piece_shape == 't2'):
            if not self.utils.is_t2_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            # go right 1 and down 2
            self.board[self.utils.get_right_column(column)][self.utils.get_2_rows_below(row)] = piece
            # go down 3
            self.board[column][self.utils.get_3_rows_below(row)] = piece
            return True

        #   x
        #   x
        # x x x
        elif (piece_shape == 'T'):
            if not self.utils.is_T_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            # go left 1 and down 2
            self.board[self.utils.get_left_column(column)][self.utils.get_2_rows_below(row)] = piece
            # go right 1 and down 2
            self.board[self.utils.get_right_column(column)][self.utils.get_2_rows_below(row)] = piece
            return True

        # x
        # x 
        # x x x
        elif (piece_shape == 'L4'):
            if not self.utils.is_L4_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            # right 1 and down 2
            self.board[self.utils.get_right_column(column)][self.utils.get_2_rows_below(row)] = piece
            # right 2 and down 2
            self.board[self.utils.get_2_right_columns(column)][self.utils.get_2_rows_below(row)] = piece
            return True

        # x
        # x x
        #   x x
        elif (piece_shape == '3'):
            if not self.utils.is_3_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go right 1 and down 1
            self.board[self.utils.get_right_column(column)][self.utils.get_row_below(row)] = piece
            # go right 1 and down 2
            self.board[self.utils.get_right_column(column)][self.utils.get_2_rows_below(row)] = piece
            # go right 2 and down 2
            self.board[self.utils.get_2_right_columns(column)][self.utils.get_2_rows_below(row)] = piece
            return True

        # x
        # x x x
        #     x
        elif (piece_shape == '4s'):
            if not self.utils.is_4s_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go right 1 and down 1
            self.board[self.utils.get_right_column(column)][self.utils.get_row_below(row)] = piece
            # go right 2 and down 1
            self.board[self.utils.get_2_right_columns(column)][self.utils.get_row_below(row)] = piece
            # go right 2 and down 2
            self.board[self.utils.get_2_right_columns(column)][self.utils.get_2_rows_below(row)] = piece
            return True

        #   x x
        # x x
        #   x
        elif (piece_shape == '7'):
            if not self.utils.is_7_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go right 1
            self.board[self.utils.get_right_column(column)][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go left 1 and down 1
            self.board[self.utils.get_left_column(column)][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece
            return True

        #   x
        # x x x
        #   x
        elif (piece_shape == '+'):
            if not self.utils.is_plus_shape_piece_valid(column, row, player_id):
                return False

            self.board[column][row] = piece
            # go down 1
            self.board[column][self.utils.get_row_below(row)] = piece
            # go right 1 and down 1
            self.board[self.utils.get_right_column(column)][self.utils.get_row_below(row)] = piece
            # go left 1 and down 1
            self.board[self.utils.get_left_column(column)][self.utils.get_row_below(row)] = piece
            # go down 2
            self.board[column][self.utils.get_2_rows_below(row)] = piece

        return True

    def remove_piece(self, column:int, row:str, piece_shape:str, player_id:int):
        self.place_piece(column, row, piece_shape, player_id, is_remove_piece=True)