class Rules:
    def __init__(self):
        self.board_rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
        self.board_columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        self.players = [1, 2]

        self.player_1_piece = self.get_green_string('1')
        self.player_2_piece = self.get_red_string('2')

        self.pieces_and_point = [
            { "shape": "o", "point": 1 },
            { "shape": "i", "point": 2 },
            { "shape": "l1", "point": 3 }, { "shape": "L1", "point": 3 },
            { "shape": "l2", "point": 4 }, { "shape": "L2", "point": 4 }, { "shape": "t", "point": 4 },
            { "shape": "O", "point": 4 }, { "shape": "z", "point": 4 },
            { "shape": "l3", "point": 5 }, { "shape": "L3", "point": 5 }, { "shape": "4", "point": 5 },
            { "shape": "6", "point": 5 }, { "shape": "C", "point": 5 }, { "shape": "t2", "point": 5 },
            { "shape": "T", "point": 5 }, { "shape": "L4", "point": 5 }, { "shape": "3", "point": 5 },
            { "shape": "4s", "point": 5 }, { "shape": "7", "point": 5 }, { "shape": "+", "point": 5 }
        ]

        self.start_positions = [
            {"column": 5, "row": "E"},
            {"column": 10, "row": "J"}
        ]

    def get_all_pieces(self) -> list:
        all_pieces = []

        for piece in self.pieces_and_point:
            all_pieces.append(piece["shape"])

        return all_pieces

    def get_piece_point(self, piece_shape: str) -> int:
        for piece in self.pieces_and_point:
            if piece["shape"] == piece_shape:
                return piece["point"]
        return 0

    def get_green_string(self, string):
        return f"\033[92m{string}\033[00m"

    def get_red_string(self, string):
        return f"\033[91m{string}\033[00m"

    def get_yellow_string(self, string):
        return f"\033[93m{string}\033[00m"

    def get_colored_string_from_player_id(self, player_id: int) -> str:
        # Apparently, a colored string is not the same as a string
        if player_id == 1:
            return self.get_green_string(str(player_id))
            
        return self.get_red_string(str(player_id))
        