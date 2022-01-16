from the_game.board import Pawn
from the_game.algorythms import (
    if_wins, best_moves, _roads_to_winning,
    _location_after_move, _if_reached_edge,
    _filter_blank, _check_if_wins, _best_roads
)

pawn_human = Pawn(0)
pawn____ai = Pawn(1)
pawn_blank = Pawn('')


def test_fitler_and_if_wins():
    pawn_b = Pawn('')
    pawn_a = Pawn(0)
    x = [[pawn_b, pawn_b], [pawn_b, pawn_a],
         [pawn_a, pawn_a]]
    y = [[pawn_b, pawn_b], [pawn_b, pawn_a],
         [pawn_a, pawn_a, pawn_b]]
    filtr = _filter_blank(x)
    filtr2 = _filter_blank(y)

    assert filtr == [[pawn_b, pawn_b], [pawn_b], []]
    assert filtr2 == [[pawn_b, pawn_b], [pawn_b], [pawn_b]]


def test_fitler2():
    pawn_b = Pawn('')
    pawn_a = Pawn(1)
    x = [[pawn_b, pawn_b], [pawn_b, pawn_a],
         [pawn_a, pawn_a]]
    y = [[pawn_b, pawn_b], [pawn_b, pawn_a],
         [pawn_a, pawn_a, pawn_b]]
    filtr = _filter_blank(x)
    filtr2 = _filter_blank(y)

    assert filtr == [[pawn_b, pawn_b], [pawn_b], []]
    assert filtr2 == [[pawn_b, pawn_b], [pawn_b], [pawn_b]]


def test_check_if_wins():
    a = Pawn('')
    b = Pawn(0)
    x = [[], [a, b]]
    y = [[a], [a, b]]
    assert _check_if_wins(y) is False
    assert _check_if_wins(x) is True


def test_best_road():
    a = Pawn('')
    b = Pawn(0)
    x = [[a, b, b], [a, b]]
    y = [[a, b, a], [a, b], [a]]
    assert _best_roads(x) == [[a, b], [a, b, b]]
    assert _best_roads(y) == [[a], [a, b], [a, b, a]]


def test_if_reached_edge():
    array = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    location_player_edge = (4, 2)
    location_player_bad = (1, 4)
    location_player_bad2 = (3, 2)
    location_ai_edge = (3, 4)
    location_ai_bad = (4, 2)
    assert _if_reached_edge(array, location_player_edge, 0) is True
    assert _if_reached_edge(array, location_player_bad, 0) is False
    assert _if_reached_edge(array, location_player_bad2, 0) is False
    assert _if_reached_edge(array, location_ai_edge, 1) is True
    assert _if_reached_edge(array, location_ai_bad, 1) is False


def test_location_after_move():
    array = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    location_down = [4, 2]
    location_right = [1, 4]
    location_middle = [3, 2]
    location_left = [3, 0]
    location_up = [0, 2]
    assert _location_after_move(array, 'up', location_up) is False
    assert _location_after_move(array, 'right', location_right) is False
    assert _location_after_move(array, 'left', location_left) is False
    assert _location_after_move(array, 'down', location_down) is False
    assert _location_after_move(array, 'down', location_up) == [1, 2]
    assert _location_after_move(array, 'left', location_right) == [1, 3]
    assert _location_after_move(array, 'right', location_middle) == [3, 3]
    assert _location_after_move(array, 'right', location_left) == [3, 1]
    assert _location_after_move(array, 'up', location_down) == [3, 2]


def test_roads_to_winning():
    array = [
        [pawn_human, pawn____ai, pawn_human],
        [pawn_human, pawn____ai, pawn_blank],
        [pawn_blank, pawn_blank, pawn_human],
    ]
    y = _roads_to_winning(array, 0)
    assert y == [[pawn_human, pawn_human, pawn_blank],
                 [pawn_human, pawn_blank, pawn_human]]


def test_if_wins():
    array = [
        [pawn_human, pawn_blank, pawn_blank, pawn_blank, pawn_blank],
        [pawn_human, pawn_blank, pawn_human, pawn_human, pawn_human],
        [pawn_human, pawn_blank, pawn_human, pawn_blank, pawn_blank],
        [pawn_human, pawn_blank, pawn_human, pawn____ai, pawn____ai],
        [pawn____ai, pawn____ai, pawn____ai, pawn____ai, pawn_blank],
    ]
    x = if_wins(array, 1)
    y = if_wins(array, 0)
    assert x is True
    assert y is False


def test_best_moves():
    '''
    Checks if gets all the winnning roads
    '''
    pawn__good = Pawn('')
    array = [
        [pawn_human, pawn__good, pawn__good, pawn__good, pawn__good],
        [pawn_human, pawn__good, pawn_human, pawn_human, pawn_human],
        [pawn_human, pawn__good, pawn_human, pawn__good, pawn__good],
        [pawn_human, pawn__good, pawn_human, pawn_blank, pawn____ai],
        [pawn____ai, pawn____ai, pawn____ai, pawn____ai, pawn__good],
    ]
    x = best_moves(array, 1)
    road = []
    for i in range(7):
        road.append(pawn__good)
    assert len(x) == 4
    assert x == [[pawn__good], [pawn_blank], [pawn_blank, pawn__good,
                 pawn__good], road]


def test_best_moves_2():
    pawn___win = Pawn('')
    pawn_winai = Pawn('')
    array = [
        [pawn_human, pawn____ai, pawn____ai, pawn____ai, pawn____ai],
        [pawn_human, pawn___win, pawn_human, pawn_human, pawn_human],
        [pawn_human, pawn____ai, pawn_human, pawn____ai, pawn_human],
        [pawn_human, pawn_winai, pawn_blank, pawn_blank, pawn_human],
        [pawn____ai, pawn____ai, pawn____ai, pawn____ai, pawn_human],
    ]
    assert best_moves(array, 0)[0] == [pawn___win]
    x = best_moves(array, 1)[0]
    assert x == [pawn_winai, pawn___win]


def test_best_moves_3():
    '''
    Should choose pawn_good{x}.
    '''
    pawn_good1 = Pawn('')
    pawn_good2 = Pawn('')
    pawn_good3 = Pawn('')
    pawn_good4 = Pawn('')
    array = [
        [pawn_human, pawn_blank, pawn_blank, pawn_blank, pawn____ai],
        [pawn_human, pawn_blank, pawn_human, pawn_good1, pawn____ai],
        [pawn_human, pawn_human, pawn_good4, pawn____ai, pawn_human],
        [pawn____ai, pawn_good2, pawn_good3, pawn_human, pawn_human],
        [pawn_blank, pawn_blank, pawn____ai, pawn_blank, pawn_human],
    ]
    x = best_moves(array, 1)
    y = [pawn_good1, pawn_good2, pawn_good3, pawn_good4]
    assert len(x[0]) == 4
    assert set(x[0]) == set(y)


def test_best_moves_4():
    '''
    Should choose pawn_good.
    '''
    pawn_good1 = Pawn('')
    pawn_good2 = Pawn('')
    array = [
        [pawn____ai, pawn_human, pawn____ai, pawn____ai, pawn_human],
        [pawn_human, pawn_blank, pawn_human, pawn____ai, pawn_human],
        [pawn_blank, pawn_blank, pawn_human, pawn____ai, pawn_human],
        [pawn_human, pawn_human, pawn_human, pawn_human, pawn_human],
        [pawn_good1, pawn____ai, pawn____ai, pawn_good2, pawn____ai],
    ]
    x = best_moves(array, 0)
    assert x[0] in ([pawn_good1], [pawn_good2])


def test_best_moves_5():
    '''
    Should start from right corner.
    + worse roads from other array[0].
    '''
    array = [
        [pawn_blank, pawn_blank, pawn_blank, pawn_blank, pawn_blank],
        [pawn____ai, pawn____ai, pawn____ai, pawn____ai, pawn_blank],
        [pawn_blank, pawn_blank, pawn_blank, pawn_blank, pawn_blank],
        [pawn_blank, pawn____ai, pawn____ai, pawn____ai, pawn____ai],
        [pawn_blank, pawn_blank, pawn_blank, pawn_blank, pawn_blank],
    ]
    x = best_moves(array, 0)
    road = []
    for i in range(9):
        road.append(pawn_blank)
    assert len(x[0]) == 9
    assert len(x) == 5
    assert x[0] == road
