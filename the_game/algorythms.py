def if_wins(board, current_player_value):
    """
    Function if_wins.
    It checks if a player won a game.
    It is checking only player, whose pawns
        are represented by a values == param:'current_player_value'.
    """
    def crossroad(array, location, current_player_value, previous_dir):
        """
        Makes a move in every direction (up, down, left, right)
            from current position.
        """
        current_pawn = (location[0], location[1])
        # checks if we were already at this location
        for pawn in ways:
            if pawn == current_pawn:
                return False
        ways.append(current_pawn)
        for i, direction in enumerate(directions):
            made_a_move = False
            # checks if we are not moving back from where we came
            if not previous_dir == directions[i - 2]:
                made_a_move = go_dir(
                    array, location, direction, current_player_value)
            if made_a_move:
                return made_a_move
        return False

    def go_dir(array, location, direction, current_player_value):
        """
        Checks:
        if a move in the param:'direction' is possible:
        - still in a board
        - still player's value
        if we reached the winning edge of the board.
        """
        loc = location[:]
        # checking if we are still within a board:
        if direction == 'up':
            if not location[0] < 1:
                loc[0] -= 1
            else:
                return False
        elif direction == 'right':
            if not location[1] > len(array[0]) - 2:
                loc[1] += 1
            else:
                return False
        elif direction == 'down':
            if not location[0] > len(array) - 2:
                loc[0] += 1
            else:
                return False
        elif direction == 'left':
            if not location[1] < 1:
                loc[1] -= 1
            else:
                return False
        # move is possible at this point
        # location is updated at this point
        # updates value of the new pawn:
        current_value = array[loc[0]][loc[1]].value
        # checks if a new pawn is players'
        if current_value != current_player_value:
            return False
        else:
            # checks if we reached the winning board edge
            if current_player_value == 0:
                if loc[0] == len(board) - 1:
                    return True
            else:
                if loc[1] == len(board[0]) - 1:
                    return True
            location = loc
            # we made a move, but did not won yet at this point
            return crossroad(array, location, current_player_value, direction)

    directions = ['down', 'right', 'up', 'left']

    player_has_won = False
    if current_player_value == 0:
        '''
        Starting from the up,
        will look for roads to get to the last row.
        '''
        for i, column in enumerate(board[0]):
            ways = []
            if column.value == current_player_value:
                player_has_won = crossroad(
                    board, [0, i], current_player_value, previous_dir=None)
                if player_has_won:
                    return player_has_won
    elif current_player_value == 1:
        '''
        Starting from the left,
        it will look for roads to get to the last column.
        '''
        for i, row in enumerate(board):
            ways = []
            pawn = row[0]
            if pawn.value == current_player_value:
                player_has_won = crossroad(
                    board, [i, 0], current_player_value, previous_dir=None)
                if player_has_won:
                    return player_has_won
    return player_has_won
