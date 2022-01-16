class Board:
    """
    Class Board.
    Represents the whole board, which contains of pawns.
    Contains attributes:
    :param _size: board's size
    :type _size: int

    :type board: array of pawns
    :type board: list of lists
    """
    def __init__(self, size=5) -> None:
        self._size = size
        self.array = self.create_board(self._size)

    def create_board(self, size):
        """
            Creates an array based on the size variable -> sets pawns values
        """
        board = []
        for row in range(size):
            board.append([])
            if row % 2 == 0:
                for column in range(size):
                    if column % 2 == 0:
                        board[row].append(Pawn(''))
                    else:
                        board[row].append(Pawn(1))
            else:
                for column in range(size):
                    if column % 2 == 0:
                        board[row].append(Pawn(0))
                    else:
                        board[row].append(Pawn(''))
        return board

    def size(self):
        return self._size


class Pawn:
    """
    Class Pawn.
    Represents a single pawn on a board.
    Contains attributes:
    :param value: pawn's value
    :type value: int

    :param _rectangle: pawn's rectangle, as an image
    :type _rectangle: pygame.Rect
    """

    def __init__(self, value) -> None:
        self.value = value
        self._rectangle = None

    def rectangle(self):
        return self._rectangle

    def set_rect(self, new_pawns_rectangle):
        self._rectangle = new_pawns_rectangle

    def set_value(self, value):
        self.value = value
