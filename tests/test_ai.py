# from the_game.board import Board, Pawn
# from the_game.AI import AIComputer, Computer


# def test_get_possible_moves():
#     '''
#     List of all posibble moves:
#     should be a list of pawn_blank
#     '''
#     pawn_human = Pawn(0)
#     pawn_ai___ = Pawn(1)
#     pawn_blank = Pawn('')
#     board = Board()
#     ai = Computer()
#     ai2 = AIComputer()
#     board.array = [
#         [pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___, pawn_blank],
#         [pawn_human, pawn_human, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_blank, pawn_human, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_blank, pawn_human, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___],
#     ]
#     assert ai.get_possible_moves(board.array) == [
#         pawn_blank, pawn_blank, pawn_blank]
#     assert ai2.get_possible_moves(board.array) == [
#         pawn_blank, pawn_blank, pawn_blank]


# def test_center():
#     '''
#     pawn_good_ is in the middle
#     AI should pick it (there is no winning/losing pawn)
#     And change its value
#     '''
#     pawn_human = Pawn(0)
#     pawn_ai___ = Pawn(1)
#     pawn_blank = Pawn('')
#     pawn_good_ = Pawn('')
#     board = Board()
#     ai = AIComputer()
#     board.array = [
#         [pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_good_, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_blank, pawn_human, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___],
#     ]
#     # if it picks it
#     assert ai.center_pawn(board.array) == pawn_good_
#     # if it chagnes its value
#     ai.play(board)
#     assert pawn_good_.value == 1


# def test_center_alread_picked():
#     '''
#     pawn in the centre is already picked
#     AI should not pick it
#     '''
#     pawn_human = Pawn(0)
#     pawn_ai___ = Pawn(1)
#     pawn_blank = Pawn('')
#     pawn_good_ = Pawn('')
#     board = Board()
#     ai = AIComputer()
#     board.array = [
#         [pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___, pawn_good_],
#         [pawn_human, pawn_human, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_human, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_blank, pawn_human, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___],
#     ]
#     # if it picks it
#     assert ai.center_pawn(board.array) is None


# def test_ai_last_ai_pawn():
#     '''
#     pawn_good_ is winning
#     AI should pick it
#     And change its value
#     '''
#     pawn_human = Pawn(0)
#     pawn_ai___ = Pawn(1)
#     pawn_blank = Pawn('')
#     pawn_good_ = Pawn('')
#     board = Board()
#     ai = AIComputer()
#     board.array = [
#         [pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___, pawn_good_],
#         [pawn_human, pawn_human, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_human, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_blank, pawn_human, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___],
#     ]
#     # if it picks it
#     assert ai.ai_last_pawn(board.array) == pawn_good_
#     # if it chagnes its value
#     ai.play(board)
#     assert pawn_good_.value == 1


# def test_ai_last_ai_pawn_2():
#     '''
#     pawn_good_ is winning
#     AI should pick it
#     And change its value
#     '''
#     pawn_human = Pawn(0)
#     pawn_ai___ = Pawn(1)
#     pawn_blank = Pawn('')
#     pawn_good_ = Pawn('')
#     board = Board()
#     ai = AIComputer()
#     board.array = [
#         [pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___, pawn_human],
#         [pawn_human, pawn_human, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_ai___, pawn_ai___, pawn_good_, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_human, pawn_blank, pawn_blank, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___],
#     ]
#     # if it picks it
#     assert ai.ai_last_pawn(board.array) == pawn_good_
#     # if it chagnes its value
#     ai.play(board)
#     assert pawn_good_.value == 1


# def test_ai_last_humans_pawn():
#     '''
#     pawn_good_ is not losing
#     AI should pick it
#     And change its value
#     '''
#     pawn_human = Pawn(0)
#     pawn_ai___ = Pawn(1)
#     pawn_blank = Pawn('')
#     pawn_good_ = Pawn('')
#     board = Board()
#     ai = AIComputer()
#     board.array = [
#         [pawn_good_, pawn_human, pawn_ai___, pawn_ai___, pawn_blank],
#         [pawn_human, pawn_human, pawn_human, pawn_ai___, pawn_human],
#         [pawn_human, pawn_ai___, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_human, pawn_blank, pawn_human, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_ai___, pawn_ai___, pawn_ai___],
#     ]
#     # if it picks it
#     assert ai.human_last_pawn(board.array) == pawn_good_
#     # if it chagnes its value
#     ai.play(board)
#     assert pawn_good_.value == 1


# def test_ai_last_humans_pawn_2():
#     '''
#     pawn_good_ is not losing
#     AI should pick it
#     And change its value
#     '''
#     pawn_human = Pawn(0)
#     pawn_ai___ = Pawn(1)
#     pawn_blank = Pawn('')
#     pawn_good_ = Pawn('')
#     board = Board()
#     ai = AIComputer()
#     board.array = [
#         [pawn_ai___, pawn_human, pawn_human, pawn_ai___, pawn_blank],
#         [pawn_human, pawn_human, pawn_human, pawn_blank, pawn_blank],
#         [pawn_blank, pawn_ai___, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_human, pawn_human, pawn_human, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_good_, pawn_ai___, pawn_ai___],
#     ]
#     # if it picks it
#     assert ai.human_last_pawn(board.array) == pawn_good_
#     # if it chagnes its value
#     ai.play(board)
#     assert pawn_good_.value == 1


# def test_easy_play(monkeypatch):
#     pawn_human = Pawn(0)
#     pawn_ai___ = Pawn(1)
#     pawn_blank = Pawn('')
#     pawn_good_ = Pawn('')
#     board = Board()
#     ai = Computer()
#     board.array = [
#         [pawn_ai___, pawn_human, pawn_human, pawn_ai___, pawn_blank],
#         [pawn_human, pawn_human, pawn_human, pawn_blank, pawn_blank],
#         [pawn_blank, pawn_ai___, pawn_human, pawn_ai___, pawn_ai___],
#         [pawn_human, pawn_human, pawn_human, pawn_human, pawn_ai___],
#         [pawn_human, pawn_ai___, pawn_good_, pawn_ai___, pawn_ai___],
#     ]

#     def choose_good(f):
#         return pawn_good_
#     monkeypatch.setattr("random.choice", choose_good)
#     ai.play(board)
#     assert pawn_good_.value == 1
