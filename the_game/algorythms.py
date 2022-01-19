def if_wins(array, _value_to_check):
    '''
    Returns bool if someone has won.
    '''
    roads = _roads_to_winning(array, _value_to_check)
    filtered_roads = _filter_blank(roads)
    has_won = _check_if_wins(filtered_roads)
    if has_won:
        return True
    return False


def best_moves(array, _value_to_check):
    '''
    Returns list of all the roads leading to win.
    Road is a list of blank pawns in this road.
    Roads are sorted from the fastest.
    '''
    roads = _roads_to_winning(array, _value_to_check)
    filtered_roads = _filter_blank(roads)
    sorted_roads = _best_roads(filtered_roads)
    return sorted_roads


def _roads_to_winning(array, _value_to_check):
    """
    Function _roads_to_winning.
    It looks for roads to win a game.
    It is finding the way to reach winning edge.
    """

    global list_of_roads
    list_of_roads = []
    possible_moves = (_value_to_check, '')
    if _value_to_check == 1:
        '''
        Starting from the left,
        it will look for roads to get to the last column.
        '''
        for i, row in enumerate(array):
            location = [i, 0]
            pawn = row[0]
            if pawn.value in possible_moves:
                # road (pawns) made from the starting point till now
                current_road = [pawn]

                # road (x, y) made from the starting point till now
                # NOTE used only to ease testing
                current_locations = [location]
                # makes move from the edge
                _crossroad(array, _value_to_check, location, current_road,
                           current_locations, previous_direction=None)

    elif _value_to_check == 0:
        '''
        Starting from the up,
        it will look for roads to get to the last row.
        '''
        for i, column in enumerate(array[0]):
            location = [0, i]
            pawn = column
            if pawn.value in possible_moves:
                # road (pawns) made from the edge till this point
                current_road = [pawn]
                # road (x, y) made from the edge till this point
                # not neccessery to run the game but allows to test
                current_locations = [location]
                _crossroad(array, _value_to_check, location, current_road,
                           current_locations, previous_direction=None)
    return list_of_roads


def _crossroad(array, value, location, current_road, locs, previous_direction):
    """
    Makes a move in every direction (up, down, left, right) \
        from current position.
    """

    directions = ['down', 'right', 'up', 'left']

    for i, direction in enumerate(directions):
        # checks if we are not moving back from where we came
        if not previous_direction == directions[i - 2]:
            road_new = _make_move(array, location, direction,
                                  current_road, locs, value)
            # if we could reach the edge
            if road_new:
                list_of_roads.append(road_new)
    # if not road found
    return road_new


def _make_move(array, location, direction, current_road, current_locs, value):
    """
    Checks:
    if a move in the param:'direction' is possible == still within a board\
    and player's/blank pawn => if not returns False\n
    if we reached the winning edge of the board => returns new_road\n
    else makes new crossroad from the new location\n
    """

    _local_location = location[:]

    # checking if we are still within a board:
    move_within_board = _location_after_move(
        array, direction, _local_location)
    if move_within_board:
        _local_location = move_within_board
    else:
        return False
    # move is within a board

    # updates value of the new pawn:
    x, y = _local_location[0], _local_location[1]
    current_value = array[x][y].value
    new_pawn = array[x][y]

    # checks if a new pawn is players'
    possible_moves = (value, '')
    if current_value not in possible_moves:
        return False
    for _location in current_locs:
        if _location == _local_location:
            return False
    else:
        # update location and road, cause we can make a move
        new_location = _local_location
        new_current_road = current_road[:]
        new_current_road.append(new_pawn)
        new_current_locs = current_locs[:]
        new_current_locs.append(location)

        # checks if we reached the winning board edge
        reached_edge = _if_reached_edge(
            array, new_location, value)
        if reached_edge:
            return new_current_road

        # we made a move, but did not reach edge yet at this point
        # so we need to go in every direction from the new location:
        return _crossroad(array, value, new_location, new_current_road,
                          new_current_locs, direction)


def _location_after_move(array, direction, location):
    '''
    Checks if after making a move in direction we are still on the board.\n
    If so then returns new location.
    '''
    if direction == 'up':
        if not location[0] < 1:
            location[0] -= 1
        else:
            return False
    elif direction == 'right':
        if not location[1] > len(array[0]) - 2:
            location[1] += 1
        else:
            return False
    elif direction == 'down':
        if not location[0] > len(array) - 2:
            location[0] += 1
        else:
            return False
    elif direction == 'left':
        if not location[1] < 1:
            location[1] -= 1
        else:
            return False
    return location


def _if_reached_edge(array, location, _value_to_check):
    '''
    Checks if current location is the winning edge.
    '''
    if _value_to_check == 1:
        if location[1] == len(array[0]) - 1:
            # we reached end at this points
            return True
    else:
        if location[0] == len(array) - 1:
            # we reached end at this points
            return True
    return False


def _filter_blank(roads):
    filtered_roads = []
    for road in roads:
        filtered_road = list(pawn for pawn in road if pawn.value == '')
        filtered_roads.append(filtered_road)
    return filtered_roads


def _check_if_wins(filtered_roads):
    for road in filtered_roads:
        if not road:
            return True
    return False


def _best_roads(filtered_roads):
    sorted_roads = list(sorted(filtered_roads, key=len))
    return sorted_roads
