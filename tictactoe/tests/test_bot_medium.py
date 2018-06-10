import pytest
from tictactoe import *

#####
#
# A move is made
#
#####

@pytest.fixture()
def g_bot_medium():
    g = start_game()
    bot_medium(g)
    return g

class Test_bot_medium(object):
    def test_type(self, g_bot_medium):
        assert isinstance(g_bot_medium, tictactoeboard)
        
    def test_board(self, g_bot_medium):
        assert g_bot_medium.board != {'11': ' ',
                                      '12': ' ',
                                      '13': ' ',
                                      '21': ' ',
                                      '22': ' ',
                                      '23': ' ',
                                      '31': ' ',
                                      '32': ' ',
                                      '33': ' '}
        
    def test_current_move(self, g_bot_medium):
        assert g_bot_medium.current_move == 'O'  

    def test_previous_move(self, g_bot_medium):
        assert g_bot_medium.previous_move == 'X'

    def test_outcome(self, g_bot_medium):
        assert g_bot_medium.outcome == None
        
#####
#
# No moves left
#
#####

def test_error_no_moves():
    with pytest.raises(ValueError) as excinfo:
        g = start_game()
        g.move("11")
        g.move("12")
        g.move("13")
        g.move("22")
        g.move("21")
        g.move("31")
        g.move("23")
        g.move("33")
        g.move("32")
        bot_medium(g)
    assert 'Board is finished' in str(excinfo.value)

#####
#
# Only one move on the board
#
#####

@pytest.fixture()
def g_bot_medium_1move():
    g = start_game()
    g.move("11")
    g.move("12")
    g.move("13")
    g.move("22")
    g.move("21")
    g.move("31")
    g.move("23")
    g.move("33")
    bot_medium(g)
    return g

class Test_bot_medium_1move(object):
    def test_type(self, g_bot_medium_1move):
        assert isinstance(g_bot_medium_1move, tictactoeboard)
        
    def test_board(self, g_bot_medium_1move):
        assert g_bot_medium_1move.board == {'11': 'X',
                                            '12': 'O',
                                            '13': 'X',
                                            '21': 'X',
                                            '22': 'O',
                                            '23': 'X',
                                            '31': 'O',
                                            '32': 'X',
                                            '33': 'O'}
        
    def test_current_move(self, g_bot_medium_1move):
        assert g_bot_medium_1move.current_move == 'O'  

    def test_previous_move(self, g_bot_medium_1move):
        assert g_bot_medium_1move.previous_move == 'X'

    def test_outcome(self, g_bot_medium_1move):
        assert g_bot_medium_1move.outcome == "Draw"

#####
#
# Winning positions available
#
#####

@pytest.fixture()
def g_bot_medium_1win():
    g = start_game()
    g.move("11")
    g.move("21")
    g.move("12")
    g.move("22")
    g.move("31")
    bot_medium(g)
    return g

class Test_bot_medium_1win(object):
    def test_type(self, g_bot_medium_1win):
        assert isinstance(g_bot_medium_1win, tictactoeboard)
        
    def test_board(self, g_bot_medium_1win):
        assert g_bot_medium_1win.board == {'11': 'X',
                                           '12': 'X',
                                           '13': ' ',
                                           '21': 'O',
                                           '22': 'O',
                                           '23': 'O',
                                           '31': 'X',
                                           '32': ' ',
                                           '33': ' '}
        
    def test_current_move(self, g_bot_medium_1win):
        assert g_bot_medium_1win.current_move == 'X'  

    def test_previous_move(self, g_bot_medium_1win):
        assert g_bot_medium_1win.previous_move == 'O'

    def test_outcome(self, g_bot_medium_1win):
        assert g_bot_medium_1win.outcome == "O win"

@pytest.fixture()
def g_bot_medium_2wins():
    g = start_game()
    g.move("22")
    g.move("21")
    g.move("11")
    g.move("31")
    g.move("12")
    g.move("32")
    bot_medium(g)
    return g

class Test_bot_medium_2wins(object):
    def test_type(self, g_bot_medium_2wins):
        assert isinstance(g_bot_medium_2wins, tictactoeboard)
        
    def test_board(self, g_bot_medium_2wins):
        assert g_bot_medium_2wins.board == {'11': 'X',
                                            '12': 'X',
                                            '13': 'X',
                                            '21': 'O',
                                            '22': 'X',
                                            '23': ' ',
                                            '31': 'O',
                                            '32': 'O',
                                            '33': ' '}
        
    def test_current_move(self, g_bot_medium_2wins):
        assert g_bot_medium_2wins.current_move == 'O'  

    def test_previous_move(self, g_bot_medium_2wins):
        assert g_bot_medium_2wins.previous_move == 'X'

    def test_outcome(self, g_bot_medium_2wins):
        assert g_bot_medium_2wins.outcome == "X win"

#####
#
# Win and block available
#
#####

@pytest.fixture()
def g_bot_medium_winblock():
    g = start_game()
    g.move("11")
    g.move("21")
    g.move("12")
    g.move("22")
    bot_medium(g)
    return g

class Test_bot_medium_winblock(object):
    def test_type(self, g_bot_medium_winblock):
        assert isinstance(g_bot_medium_winblock, tictactoeboard)
        
    def test_board(self, g_bot_medium_winblock):
        assert g_bot_medium_winblock.board == {'11': 'X',
                                               '12': 'X',
                                               '13': 'X',
                                               '21': 'O',
                                               '22': 'O',
                                               '23': ' ',
                                               '31': ' ',
                                               '32': ' ',
                                               '33': ' '}
        
    def test_current_move(self, g_bot_medium_winblock):
        assert g_bot_medium_winblock.current_move == 'O'  

    def test_previous_move(self, g_bot_medium_winblock):
        assert g_bot_medium_winblock.previous_move == 'X'

    def test_outcome(self, g_bot_medium_winblock):
        assert g_bot_medium_winblock.outcome == "X win"
        
#####
#
# Only block available
#
#####

@pytest.fixture()
def g_bot_medium_block():
    g = start_game()
    g.move("11")
    g.move("21")
    g.move("31")
    g.move("22")
    bot_medium(g)
    return g

class Test_bot_medium_block(object):
    def test_type(self, g_bot_medium_block):
        assert isinstance(g_bot_medium_block, tictactoeboard)
        
    def test_board(self, g_bot_medium_block):
        assert g_bot_medium_block.board == {'11': 'X',
                                               '12': ' ',
                                               '13': ' ',
                                               '21': 'O',
                                               '22': 'O',
                                               '23': 'X',
                                               '31': 'X',
                                               '32': ' ',
                                               '33': ' '}
        
    def test_current_move(self, g_bot_medium_block):
        assert g_bot_medium_block.current_move == 'O'  

    def test_previous_move(self, g_bot_medium_block):
        assert g_bot_medium_block.previous_move == 'X'

    def test_outcome(self, g_bot_medium_block):
        assert g_bot_medium_block.outcome == None