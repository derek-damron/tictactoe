from copy import copy

def bot_intermediate(game):
    possible_moves = game.available_moves()
    
    # Special cases - No moves left or only one move left
    if len(possible_moves) == 0:
        raise ValueError('Board is finished')
    elif len(possible_moves) == 1:
        game.move(possible_moves[0])
        return
    
    # Make any winning moves on the board
    winning_moves = []
    for m in possible_moves:
        game_copy = copy(game)
        game_copy.move(m)
        if game_copy.is_win():
            winning_moves += [m]
    if len(winning_moves) > 0:
        game.move(winning_moves[0])
        return
        
    # If no winning moves on the board, make any blocking moves
    blocking_moves = []
    for m in possible_moves:
        game_copy = copy(game)
        game_copy.switch_sides()
        game_copy.move(m)
        if game_copy.is_win():
            blocking_moves += [m]
    if len(blocking_moves) > 0:
        game.move(blocking_moves[0])
        return
        
    # Else make a random move
    bot_random(game)
    return