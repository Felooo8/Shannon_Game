import random
import names
from the_game.algorythms import best_moves


class Computer:
    """
    Class Computer.
    Represents an AI.`
    It makes random moves.\n
    Contains attributes:\n
    :param name: AI's name\n
    :type name: str
    """

    def __init__(self):
        self.name = names.get_first_name()

    def play(self, board):
        '''
        Function play.
        Makes AI's move => chooses random free place and puts pawn there.
        '''
        possible_moves = self._get_possible_moves(board.array)
        if possible_moves:
            x = random.choice(possible_moves)
            x.set_value(1)

    def _get_possible_moves(self, board):
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
    It makes moves based on a simple algorythm.\n
    Contains attributes:
    :param name: AI's name
    :type name: str
    """

    def __init__(self):
        return super().__init__()

    def play(self, board):
        '''
        Function play.
        Makes AI's move based on the algorythm =>
        checks who can win first and chooses one of the pawns on this road.
        '''
        array = board.array

        # gets player's winning roads
        best_ai_moves = self._winning_roads(array, 1)
        # checks how many moves ai needs to win
        best_ai = self._best_road_lenght(best_ai_moves)
        # gets ai's winning roads
        best_player_moves = self._winning_roads(array, 0)
        # checks how many moves player needs to win
        best_player = self._best_road_lenght(best_player_moves)

        # checks if player can win first
        if best_player < best_ai:
            fastest_moves = self._fastest_roads(best_player_moves)
            move = self._random_move(fastest_moves)
        else:
            fastest_moves = self._fastest_roads(best_ai_moves)
            move = self._random_move(fastest_moves)
        move.set_value(1)
        return

    def _random_move(self, roads):
        '''
        Returns random element from random list in array.
        '''
        choice = random.choice(random.choice(roads))
        return choice

    def _winning_roads(self, array, value_to_check):
        '''
        Returns list of the winning roads.
        '''
        winning_roads = best_moves(array, value_to_check)
        return winning_roads

    def _best_road_lenght(self, moves):
        '''
        Returns lenght of the fastest road.
        lenght = number of moves to win
        '''
        lenght = len(moves[0])
        return lenght

    def _fastest_roads(self, moves):
        '''
        Returns list of fastest roads (if their lenght is equal).
        lenght = number of moves to win
        '''
        best_roads = []
        count = None
        for road in moves:
            lenght = len(road)
            if count is None:
                count = lenght
                best_roads = [road]
            elif lenght < count:
                count = lenght
                best_roads = [road]
            elif lenght == count:
                best_roads.append(road)
        return best_roads
