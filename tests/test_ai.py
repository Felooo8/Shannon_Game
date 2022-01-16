from the_game.board import Board, Pawn
from the_game.AI import AIComputer, Computer

pawn_human = Pawn(0)
pawn____ai = Pawn(1)
pawn__wall = Pawn(2)  # will be skipped
pawn_blank = Pawn('')


# TESTING EASY AI
def test_get_possible_moves():
    '''
    List of all posibble moves:
    should be a list of pawn_blank
    '''
    board = Board()
    ai = Computer()
    board.array = [
        [pawn____ai, pawn____ai, pawn____ai, pawn____ai, pawn_blank],
        [pawn_human, pawn_human, pawn_human, pawn____ai, pawn____ai],
        [pawn_human, pawn_blank, pawn_human, pawn____ai, pawn_human],
        [pawn_human, pawn_human, pawn_blank, pawn_human, pawn____ai],
        [pawn_human, pawn____ai, pawn____ai, pawn____ai, pawn____ai],
    ]
    assert ai._get_possible_moves(board.array) == [
        pawn_blank, pawn_blank, pawn_blank]


def test_easy_play(monkeypatch):
    pawn_good_ = Pawn('')
    board = Board()
    ai = Computer()
    board.array = [
        [pawn____ai, pawn_human, pawn_human, pawn____ai, pawn_blank],
        [pawn_human, pawn_human, pawn_human, pawn_blank, pawn_blank],
        [pawn_blank, pawn____ai, pawn_human, pawn____ai, pawn____ai],
        [pawn_human, pawn_human, pawn_human, pawn_human, pawn____ai],
        [pawn_human, pawn____ai, pawn_good_, pawn____ai, pawn____ai],
    ]

    def choose_good(f):
        return pawn_good_
    monkeypatch.setattr("random.choice", choose_good)
    ai.play(board)
    assert pawn_good_.value == 1


# TESTING HARD AI
def test_winning_fastest_roads():
    '''
    Checks if gets all the winnning roads
    '''
    pawn__good = Pawn('')
    board = Board()
    ai = AIComputer()
    board.array = [
        [pawn_human, pawn__good, pawn__good, pawn__good, pawn__good],
        [pawn_human, pawn__good, pawn_human, pawn_human, pawn_human],
        [pawn_human, pawn__good, pawn_human, pawn__good, pawn__good],
        [pawn_human, pawn__good, pawn_human, pawn_blank, pawn____ai],
        [pawn____ai, pawn____ai, pawn____ai, pawn____ai, pawn__good],
    ]
    x = ai._winning_roads(board.array, 1)
    road = []
    for i in range(7):
        road.append(pawn__good)
    assert len(x) == 4
    assert x == [[pawn__good], [pawn_blank], [pawn_blank, pawn__good,
                 pawn__good], road]
    fastest = ai._fastest_roads(x)
    assert fastest == [[pawn__good], [pawn_blank]]


def test_best_road_lenght():
    board = Board()
    ai = AIComputer()
    board.array = [
        [pawn_human, pawn_blank, pawn_blank, pawn_blank, pawn_blank],
        [pawn_human, pawn_blank, pawn_human, pawn_human, pawn_human],
        [pawn_human, pawn_blank, pawn_human, pawn_blank, pawn_blank],
        [pawn_human, pawn_blank, pawn_human, pawn_blank, pawn____ai],
        [pawn____ai, pawn____ai, pawn____ai, pawn____ai, pawn_blank],
    ]
    x = [[pawn_blank], [pawn_blank], [pawn_blank, pawn_blank]]
    assert ai._best_road_lenght(x) == 1


def test_hard_play_1():
    '''
    Should choose pawn_good.
    '''
    pawn__good = Pawn('')
    board = Board()
    ai = AIComputer()
    board.array = [
        [pawn_human, pawn__wall, pawn__wall, pawn__wall, pawn__wall],
        [pawn_human, pawn__wall, pawn_blank, pawn_blank, pawn_blank],
        [pawn_human, pawn__wall, pawn_blank, pawn_blank, pawn_blank],
        [pawn__good, pawn__wall, pawn__wall, pawn__wall, pawn__wall],
        [pawn__good, pawn____ai, pawn____ai, pawn_blank, pawn_blank],
    ]
    ai.play(board)
    assert pawn__good.value == 1


def test_hard_play_2():
    '''
    Should choose pawn_good.
    '''
    pawn_good1 = Pawn('')
    pawn_good2 = Pawn('')
    pawn_good3 = Pawn('')
    pawn_good4 = Pawn('')
    board = Board()
    ai = AIComputer()
    board.array = [
        [pawn_human, pawn_blank, pawn_blank, pawn_blank, pawn____ai],
        [pawn_human, pawn_blank, pawn_blank, pawn_blank, pawn____ai],
        [pawn_human, pawn_good1, pawn_good4, pawn____ai, pawn_human],
        [pawn____ai, pawn_good2, pawn_good3, pawn_human, pawn_human],
        [pawn_blank, pawn_blank, pawn____ai, pawn_blank, pawn_human],
    ]
    ai.play(board)
    assert 1 in (pawn_good1.value, pawn_good2.value,
                 pawn_good3.value, pawn_good4.value)


def test_hard_play_3():
    '''
    Should choose pawn_good.
    '''
    pawn_good1 = Pawn('')
    pawn_good2 = Pawn('')
    board = Board()
    ai = AIComputer()
    board.array = [
        [pawn____ai, pawn____ai, pawn____ai, pawn____ai, pawn_human],
        [pawn_human, pawn_blank, pawn_human, pawn____ai, pawn_human],
        [pawn_blank, pawn_blank, pawn_human, pawn____ai, pawn_human],
        [pawn_human, pawn_human, pawn_human, pawn_human, pawn_human],
        [pawn_good1, pawn____ai, pawn____ai, pawn_good2, pawn____ai],
    ]
    ai.play(board)
    assert 1 in (pawn_good1.value, pawn_good2.value)


def test_hard_play_4():
    '''
    Should choose pawn_good.
    '''
    pawn_good1 = Pawn('')
    board = Board()
    ai = AIComputer()
    board.array = [
        [pawn_human, pawn____ai, pawn____ai, pawn____ai, pawn_good1],
        [pawn_human, pawn____ai, pawn_human, pawn_human, pawn_human],
        [pawn____ai, pawn____ai, pawn_human, pawn____ai, pawn_blank],
        [pawn_human, pawn_human, pawn_human, pawn_blank, pawn_human],
        [pawn_blank, pawn____ai, pawn_blank, pawn____ai, pawn_blank],
    ]
    ai.play(board)
    assert pawn_good1.value == 1


def test_hard_play_7x7():
    '''
    Should choose g.
    '''
    h = Pawn(0)
    a = Pawn(1)
    b = Pawn(2)  # will be skipped
    g = Pawn('')
    z = Pawn('')
    board = Board()
    ai = AIComputer()
    board.array = [
        [h, b, b, b, b, b, b],
        [h, b, b, b, b, b, b],
        [h, b, b, b, b, b, b],
        [h, b, b, b, b, b, b],
        [h, b, b, b, b, b, b],
        [h, b, b, b, b, b, b],
        [g, z, a, a, a, a, a]
    ]

    ai.play(board)
    assert g.value == 1
