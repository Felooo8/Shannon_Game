# from the_game.board import Board, Pawn
# from the_game.algorythms import if_wins

# pawn_human = Pawn(0)
# pawn_ai___ = Pawn(1)
# pawn_blank = Pawn('')

# # def test_game():
# #     AI = Computer(0)
# #     game = Game(AI)
# #     assert game.human_move_now == True
# #     assert game.human_player_value == 0
# #     assert game.pc_player_value == 1


# def test_if_wins_human():
#     board = Board()
#     board.array = [
#         [pawn_ai___, pawn_ai___, pawn_human, pawn_ai___, pawn_blank],
#         [pawn_human, pawn_ai___, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_human, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_blank, pawn_human, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___],
#     ]
#     assert if_wins(board.array, 0) is False


# def test_if_wins_human_2():
#     board = Board()
#     board.array = [
#         [pawn_ai___, pawn_ai___, pawn_blank, pawn_ai___, pawn_blank],
#         [pawn_human, pawn_human, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_human, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_blank, pawn_human, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___],
#     ]
#     assert if_wins(board.array, 0) is False


# def test_if_wins_human_3():
#     board = Board()
#     board.array = [
#         [pawn_human, pawn_ai___, pawn_blank, pawn_ai___, pawn_blank],
#         [pawn_human, pawn_human, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_human, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_blank, pawn_human, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___],
#     ]
#     assert if_wins(board.array, 0) is True


# def test_if_wins_human_4():
#     board = Board()
#     board.array = [
#         [pawn_human, pawn_ai___, pawn_blank, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_human, pawn_ai___, pawn_human],
#         [pawn_human, pawn_ai___, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_human, pawn_human, pawn_blank, pawn_human],
#         [pawn_ai___, pawn_ai___, pawn_human, pawn_ai___, pawn_human],
#     ]
#     assert if_wins(board.array, 0) is True

# def test_if_wins_human_5():
#     board = Board()
#     board.array = [
#         [pawn_ai___, pawn_ai___, pawn_blank, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_human, pawn_human, pawn_human],
#         [pawn_ai___, pawn_ai___, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_human, pawn_human, pawn_blank, pawn_human],
#         [pawn_human, pawn_ai___, pawn_blank, pawn_ai___, pawn_human],
#     ]
#     assert if_wins(board.array, 0) is True


# def test_no_RecursionError():
#     board = Board()
#     board.array = [
#         [pawn_human, pawn_ai___, pawn_blank, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_human, pawn_ai___, pawn_human],
#         [pawn_human, pawn_ai___, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_human, pawn_human, pawn_blank, pawn_human],
#         [pawn_ai___, pawn_ai___, pawn_blank, pawn_ai___, pawn_human],
#     ]
#     assert if_wins(board.array, 0) is False


# def test_if_wins_ai_1():
#     board = Board()
#     board.array = [
#         [pawn_ai___, pawn_ai___, pawn_blank, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_human, pawn_human, pawn_human],
#         [pawn_ai___, pawn_ai___, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_human, pawn_human, pawn_blank, pawn_human],
#         [pawn_human, pawn_ai___, pawn_blank, pawn_ai___, pawn_human],
#     ]
#     assert if_wins(board.array, 1) is False


# def test_if_wins_ai_2():
#     board = Board()
#     board.array = [
#         [pawn_ai___, pawn_ai___, pawn_ai___, pawn_blank, pawn_ai___],
#         [pawn_ai___, pawn_human, pawn_human, pawn_human, pawn_ai___],
#         [pawn_ai___, pawn_ai___, pawn_blank, pawn_ai___, pawn_ai___],
#         [pawn_ai___, pawn_human, pawn_human, pawn_blank, pawn_ai___],
#         [pawn_ai___, pawn_ai___, pawn_blank, pawn_ai___, pawn_ai___],
#     ]
#     assert if_wins(board.array, 1) is False


# def test_if_wins_ai_3():
#     board = Board()
#     board.array = [
#         [pawn_ai___, pawn_ai___, pawn_blank, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_human, pawn_human, pawn_human],
#         [pawn_ai___, pawn_ai___, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_human, pawn_blank, pawn_human],
#         [pawn_human, pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___],
#     ]
#     assert if_wins(board.array, 1) is True


# def test_if_wins_ai_4():
#     board = Board()
#     board.array = [
#         [pawn_ai___, pawn_ai___, pawn_blank, pawn_ai___, pawn_human],
#         [pawn_human, pawn_ai___, pawn_human, pawn_human, pawn_human],
#         [pawn_ai___, pawn_ai___, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___, pawn_human],
#         [pawn_human, pawn_ai___, pawn_blank, pawn_ai___, pawn_human],
#     ]
#     assert if_wins(board.array, 1) is True


# def test_no_RecursionError_ai():
#     board = Board()
#     board.array = [
#         [pawn_human, pawn_ai___, pawn_blank, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_human, pawn_ai___, pawn_human],
#         [pawn_human, pawn_ai___, pawn_ai___, pawn_ai___, pawn_blank],
#         [pawn_human, pawn_ai___, pawn_human, pawn_ai___, pawn_human],
#         [pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___, pawn_human],
#     ]
#     assert if_wins(board.array, 1) is False
