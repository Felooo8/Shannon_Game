import random
import names


class Computer:
    """
    Class Computer.
    Represents an AI.
    It makes random moves.
    Contains attributes:
    :param name: AI's name
    :type name: str
    """
    def __init__(self):
        self.name = names.get_first_name()

    def play(self, board):
        possible_moves = self.get_possible_moves(board.array)
        if possible_moves:
            x = random.choice(possible_moves)
            x.set_value(1)

    def get_possible_moves(self, board):
        possible_moves = []
        for row in board:
            for pawn in row:
                if pawn.value == '':
                    possible_moves.append(pawn)
        return possible_moves


class AIComputer(Computer):
    """
    Class Computer.
    Represents an advanced AI.
    It makes moves based on a simple algorythm.
    Contains attributes:
    :param name: AI's name
    :type name: str
    """
    def __init__(self):
        return super().__init__()

    def play(self, board):
        array = board.array
        possible_moves = self.get_possible_moves(array)
        last_ai_missing_pawn = self.ai_last_pawn(array)
        if last_ai_missing_pawn:
            last_ai_missing_pawn.set_value(1)
            return
        last_humans_missing_pawn = self.human_last_pawn(array)
        if last_humans_missing_pawn:
            last_humans_missing_pawn.set_value(1)
            return
        if possible_moves:
            # tries to pick center pawn if possible
            center_pawn = self.center_pawn(array)
            if center_pawn:
                center_pawn.set_value(1)
            else:
                x = random.choice(possible_moves)
                x.set_value(1)
            return

    def get_possible_moves(self, board):
        return super().get_possible_moves(board)

    def center_pawn(self, array):
        center = len(array) // 2
        center_pawn = array[center][center]
        if center_pawn.value == '':
            return center_pawn
        else:
            return None

    def ai_last_pawn(self, array):
        for row in array:
            pawns_values = list(pawn.value for pawn in row)
            if pawns_values.count(1) == len(array) - 1:
                for pawn in row:
                    if pawn.value == '':
                        return pawn
        return None

    def human_last_pawn(self, array):
        for i in range(len(array[0])):
            column = list(item[i] for item in array)
            pawns_values = list(pawn.value for pawn in column)
            if pawns_values.count(0) == len(array) - 1:
                for pawn in column:
                    if pawn.value == '':
                        return pawn
        return None
