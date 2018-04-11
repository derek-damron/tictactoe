from random import sample

def bot_random(self):
    possible_moves = self.available_moves()
    random_move = [ possible_moves[i] for i in sorted(sample(range(len(possible_moves)), 1)) ][0]
    self.move(random_move)