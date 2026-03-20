"""Computer opponents for the Shannon game."""

from __future__ import annotations

import random
from typing import Iterable

from the_game.algorythms import best_moves

_DEFAULT_AI_NAMES = (
    "Ada",
    "Claude",
    "Edsger",
    "Grace",
    "Shannon",
    "Turing",
)

try:
    import names as _names  # type: ignore
except ImportError:  # pragma: no cover - exercised indirectly in tests/envs without names
    _names = None


def _generate_ai_name() -> str:
    """Return a readable AI name without requiring optional third-party packages."""
    if _names is not None:
        return _names.get_first_name()
    return random.choice(_DEFAULT_AI_NAMES)


class Computer:
    """Easy AI that plays a random valid move."""

    def __init__(self) -> None:
        self.name = _generate_ai_name()

    def play(self, board) -> None:
        """Choose a random free pawn and claim it for the AI."""
        possible_moves = self._get_possible_moves(board.array)
        if possible_moves:
            random.choice(possible_moves).set_value(1)

    def _get_possible_moves(self, board) -> list:
        return [pawn for row in board for pawn in row if pawn.value == ""]


class AIComputer(Computer):
    """Heuristic AI that tries to optimize its fastest winning path."""

    def play(self, board) -> None:
        """Choose a move from the shortest available path to victory or defense."""
        array = board.array

        ai_winning_moves = self._winning_roads(array, 1)
        ai_fastest_win = self._best_road_length(ai_winning_moves)

        player_winning_moves = self._winning_roads(array, 0)
        player_fastest_win = self._best_road_length(player_winning_moves)

        if player_fastest_win < ai_fastest_win:
            fastest_moves = self._fastest_roads(player_winning_moves)
        else:
            fastest_moves = self._fastest_roads(ai_winning_moves)

        self._random_move(fastest_moves).set_value(1)

    def _random_move(self, roads: Iterable[list]):
        """Return a random candidate move from a random candidate road."""
        return random.choice(random.choice(list(roads)))

    def _winning_roads(self, array, value_to_check):
        """Return every candidate road to victory for the requested side."""
        return best_moves(array, value_to_check)

    def _best_road_length(self, moves) -> int:
        """Return the length of the shortest path to victory."""
        return len(moves[0])

    def _best_road_lenght(self, moves) -> int:  # backwards-compatible legacy name
        return self._best_road_length(moves)

    def _fastest_roads(self, moves):
        """Return every road tied for the current best length."""
        best_roads = []
        count = None
        for road in moves:
            length = len(road)
            if count is None:
                count = length
                best_roads = [road]
            elif length < count:
                count = length
                best_roads = [road]
            elif length == count:
                best_roads.append(road)
        return best_roads
