from the_game.player import Player


def test_player():
    player = Player()
    assert player.name == 'Player 1'
    player2 = Player('Felo')
    assert player2.name == 'Felo'
