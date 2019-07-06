from random import choice

def bot_easy(game):
    possible_moves = game.available_moves()
    random_move = choice(possible_moves)
    game.move(random_move)