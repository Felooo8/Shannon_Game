# from the_game.board import Board, Pawn


# def test_init():
#     board = Board(5)
#     assert board._size == 5
#     assert board.size() == 5
#     array_values = [[pawn.value for pawn in row] for row in board.array]
#     assert array_values == [
#         ['', 1, '', 1, ''],
#         [0, '', 0, '', 0],
#         ['', 1, '', 1, ''],
#         [0, '', 0, '', 0],
#         ['', 1, '', 1, ''],
#     ]


# def test_init_7():
#     board = Board(7)
#     assert board._size == 7
#     assert board.size() == 7
#     array_values = [[pawn.value for pawn in row] for row in board.array]
#     assert array_values == [
#         ['', 1, '', 1, '', 1, ''],
#         [0, '', 0, '', 0, '', 0],
#         ['', 1, '', 1, '', 1, ''],
#         [0, '', 0, '', 0, '', 0],
#         ['', 1, '', 1, '', 1, ''],
#         [0, '', 0, '', 0, '', 0],
#         ['', 1, '', 1, '', 1, ''],
#     ]


# def test_pawn():
#     pawn_human = Pawn(0)
#     pawn_ai___ = Pawn(1)
#     pawn_blank = Pawn('')
#     assert pawn_human.value == 0
#     assert pawn_ai___.value == 1
#     assert pawn_blank.value == ''
#     pawn_human.set_value(1)
#     pawn_ai___.set_value(0)
#     pawn_blank.set_value(1)
#     assert pawn_human.value == 1
#     assert pawn_ai___.value == 0
#     assert pawn_blank.value == 1
