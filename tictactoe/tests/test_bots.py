import pytest
from tictactoe import *

#####
#
# Random bot
#
####

@pytest.fixture()
def g_bot_random():
    g = play_game()
    bot_random(g)
    return g

class Test_bot_random(object):
    def test_type(self, g_bot_random):
        assert isinstance(g_bot_random, tictactoeboard)
        
    def test_board(self, g_bot_random):
        assert g_bot_random.board != {'11': ' ',
                                      '12': ' ',
                                      '13': ' ',
                                      '21': ' ',
                                      '22': ' ',
                                      '23': ' ',
                                      '31': ' ',
                                      '32': ' ',
                                      '33': ' '}
        
    def test_current_move(self, g_bot_random):
        assert g_bot_random.current_move == 'O'  

    def test_previous_move(self, g_bot_random):
        assert g_bot_random.previous_move == 'X'

    def test_outcome(self, g_bot_random):
        assert g_bot_random.outcome == None