from random import sample

def bot_easy(game):
    possible_moves = game.available_moves()
    random_move = [ possible_moves[i] for i in sorted(sample(range(len(possible_moves)), 1)) ][0]
    game.move(random_move)