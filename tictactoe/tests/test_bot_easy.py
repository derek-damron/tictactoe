import pytest
from tictactoe import *

@pytest.fixture()
def g_bot_easy():
    g = start_game()
    bot_easy(g)
    return g

class Test_bot_easy(object):
    def test_type(self, g_bot_easy):
        assert isinstance(g_bot_easy, tictactoeboard)
        
    def test_board(self, g_bot_easy):
        assert g_bot_easy.board != {'11': ' ',
                                    '12': ' ',
                                    '13': ' ',
                                    '21': ' ',
                                    '22': ' ',
                                    '23': ' ',
                                    '31': ' ',
                                    '32': ' ',
                                    '33': ' '}
        
    def test_current_move(self, g_bot_easy):
        assert g_bot_easy.current_move == 'O'  

    def test_previous_move(self, g_bot_easy):
        assert g_bot_easy.previous_move == 'X'

    def test_outcome(self, g_bot_easy):
        assert g_bot_easy.outcome == None
