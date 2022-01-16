from the_game.AI import AIComputer, Computer
from the_game.board import Board
from the_game.window import Window
from the_game.player import Player
from the_game.algorythms import if_wins


class Game:
    """
    Class Game.
    Runs a game.
    Contains attributes:
    :param human_player_value: determines, what is the value of human's pawn
    :type human_player_value: int

    :param pc_player_value: determines, what is the value of ai's pawn
    :type pc_player_value: int
    """
    def __init__(self, player=None, board_size=5, AI=None):
        self.human_move_now = True
        if AI is None:
            AI = Computer()
        self.AI = AI
        if player is None:
            player = Player()
        self.player = player

        self.board_size = board_size

        self._human_player_value = 0
        self._pc_player_value = 1

        self.window = Window()

        self.create_board()

    def create_board(self):
        self.board = Board(self.board_size)

    def start(self):
        """
        Runs a starting window, which allow a player to choose:
        name, board size and AI level
        """
        board_size = 5
        ai_level = 0
        name = ''

        # if player clicked at the name input field
        input_is_active = False

        run = True
        while run:
            # creates a window and gets players choices
            play, name, board_size, ai_level, updated_input_is_active = (
                self.window.draw_start_window(
                    board_size, ai_level, name, input_is_active))

            self.player.name = name
            self.board_size = board_size
            if ai_level == 0:
                AI = Computer()
            else:
                AI = AIComputer()
            self.AI = AI

            input_is_active = updated_input_is_active

            self.create_board()

            self.window.set_bg(self.board_size)

            # if finished setting up his game
            if play:
                if self.player.name == '':
                    self.player.name = 'Player 1'
                return

    def play(self):
        run = True
        while run:
            self.draw_window()

            # checks if now is players move and if so, checks if he made a move
            if self.human_move_now:
                pawn = self.window.handle_events(
                    self.board.array, self.human_move_now)

                # checks if player made a move
                if pawn:
                    self.move_was_made(pawn)
                    self.change_current_player()
            else:
                # now is AI's move -> makes a move
                self.AI.play(self.board)
                self.window.wait()  # delay
                self.change_current_player()

    def draw_window(self):
        self.window.draw_main_window(self.board, self._human_player_value,
                                     self._pc_player_value)

    def move_was_made(self, pawn):
        """
        Sets chosen pawn's value to a value assigned to a human player
        """
        pawn.set_value(self._human_player_value)

    def change_current_player(self):
        """
        Cheks if someone has won, after his move, then changes current mover
        """
        self.check_if_someone_wins()
        self.human_move_now = not self.human_move_now

    def check_if_someone_wins(self):
        """
        Checks if someone has won after the last move
        """
        # gets value which has just changed
        value = (self._human_player_value if self.human_move_now
                 else self._pc_player_value)
        x = if_wins(self.board.array, value)
        if x:
            self.if_someone_wins()

    def if_someone_wins(self):
        """
        Handles action after someone has won
        """

        run = True
        while run:
            if self.human_move_now:
                self.window.draw_end(self.player.name, self.board,
                                     self._human_player_value,
                                     self._pc_player_value)
            else:
                self.window.draw_end(self.AI.name, self.board,
                                     self._human_player_value,
                                     self._pc_player_value)
