# from the_game.board import Board
# from the_game.game import Game
# from the_game.AI import Computer, AIComputer
# from the_game.player import Player
# from the_game.window import Window
# from the_game.board import Board, Pawn
# from the_game.algorythms import if_wins
# import pytest


# def test_init_blank():
#     game = Game()
#     assert game.human_move_now is True
#     assert type(game.AI) is Computer
#     assert type(game.player) is Player
#     assert game.board_size == 5
#     assert game._human_player_value == 0
#     assert game._pc_player_value == 1
#     assert type(game.window) is Window
#     assert type(game.board) is Board
#     assert game.board._size == game.board_size == 5


# def test_init(monkeypatch):
#     def name():
#         return "Test"

#     monkeypatch.setattr("names.get_first_name", name)
#     player = Player()
#     ai = Computer()
#     game = Game(player, 7, ai)
#     assert game.AI == ai
#     assert game.AI.name == ai.name == "Test"
#     assert game.player.name == "Player 1"
#     assert game.board_size == 7
#     assert game.board._size == game.board_size == 7


# def test_change_player():
#     game = Game()
#     assert game.human_move_now is True
#     game.change_current_player()
#     assert game.human_move_now is False


# def test_move_was_made():
#     pawn_blank = Pawn('')
#     game = Game()
#     assert pawn_blank.value == ''
#     game.move_was_made(pawn_blank)
#     assert pawn_blank.value == game._human_player_value


# def test_start(monkeypatch):
#     def returnValues(a, b, c, d, e):
#         return True, "Felo", 7, 1, 0

#     monkeypatch.setattr("the_game.game.Window.draw_start_window", returnValues)
#     player = Player()
#     ai = Computer()
#     game = Game(player, 5, ai)
#     game.start()
#     assert type(game.AI) == AIComputer
#     assert game.player.name == "Felo"
#     assert game.board_size == 7


# def test_main(monkeypatch):
#     def returnPawn(a, b, c):
#         return pawn_blank

#     def raiseError(a):
#         raise ValueError

#     monkeypatch.setattr("the_game.game.Window.handle_events", returnPawn)
#     monkeypatch.setattr("the_game.game.Game.change_current_player", raiseError)
#     pawn_blank = Pawn('')
#     game = Game()
#     game.window.set_bg(game.board_size)
#     with pytest.raises(ValueError):
#         game.play()
#     assert pawn_blank.value == game._human_player_value
