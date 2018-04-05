import pytest
from tictactoe import *

#####
#
# Draw
#
####

@pytest.fixture()
def g_draw():
    g = play_game()
    g.move('11')
    g.move('12')
    g.move('13')
    g.move('21')
    g.move('23')
    g.move('22')
    g.move('31')
    g.move('33')
    g.move('32')
    return g

class Test_draw(object):
    def test_outcome(self, g_draw):
        assert g_draw.outcome == "Draw"

    def test_available_moves(self, g_draw):
        assert g_draw.available_moves() == []

    def test_are_moves_left(self, g_draw):
        assert g_draw.are_moves_left() == False

    def test_is_win(self, g_draw):
        assert g_draw.is_win() == False

    def test_print(self, g_draw, capsys):
        print(g_draw)
        out, err = capsys.readouterr()
        assert out == ' X | O | X \n-----------\n O | O | X \n-----------\n X | X | O ' + '\n'

#####
#
# Wins
#
####

@pytest.fixture()
def g_row_1_win():
    g = play_game()
    g.move('11')
    g.move('21')
    g.move('12')
    g.move('22')
    g.move('13')
    return g

class Test_row_1_win(object):
    def test_outcome(self, g_row_1_win):
        assert g_row_1_win.outcome == "X win"

    def test_is_win(self, g_row_1_win):
        assert g_row_1_win.is_win() == True

@pytest.fixture()
def g_row_2_win():
    g = play_game()
    g.move('11')
    g.move('21')
    g.move('12')
    g.move('22')
    g.move('31')
    g.move('23')
    return g

class Test_row_2_win(object):
    def test_outcome(self, g_row_2_win):
        assert g_row_2_win.outcome == "O win"

    def test_is_win(self, g_row_2_win):
        assert g_row_2_win.is_win() == True

@pytest.fixture()
def g_row_3_win():
    g = play_game()
    g.move('31')
    g.move('21')
    g.move('32')
    g.move('22')
    g.move('33')
    return g

class Test_row_3_win(object):
    def test_outcome(self, g_row_3_win):
        assert g_row_3_win.outcome == "X win"

    def test_is_win(self, g_row_3_win):
        assert g_row_3_win.is_win() == True

@pytest.fixture()
def g_col_1_win():
    g = play_game()
    g.move('11')
    g.move('12')
    g.move('21')
    g.move('22')
    g.move('31')
    return g

class Test_col_1_win(object):
    def test_outcome(self, g_col_1_win):
        assert g_col_1_win.outcome == "X win"

    def test_is_win(self, g_col_1_win):
        assert g_col_1_win.is_win() == True

@pytest.fixture()
def g_col_2_win():
    g = play_game()
    g.move('11')
    g.move('12')
    g.move('21')
    g.move('22')
    g.move('13')
    g.move('32')
    return g

class Test_col_2_win(object):
    def test_outcome(self, g_col_2_win):
        assert g_col_2_win.outcome == "O win"

    def test_is_win(self, g_col_2_win):
        assert g_col_2_win.is_win() == True

@pytest.fixture()
def g_col_3_win():
    g = play_game()
    g.move('13')
    g.move('12')
    g.move('23')
    g.move('22')
    g.move('33')
    return g

class Test_col_3_win(object):
    def test_outcome(self, g_col_3_win):
        assert g_col_3_win.outcome == "X win"

    def test_is_win(self, g_col_3_win):
        assert g_col_3_win.is_win() == True

@pytest.fixture()
def g_diag_upper_left_win():
    g = play_game()
    g.move('11')
    g.move('12')
    g.move('22')
    g.move('23')
    g.move('33')
    return g

class Test_diag_upper_left_win(object):
    def test_outcome(self, g_diag_upper_left_win):
        assert g_diag_upper_left_win.outcome == "X win"

    def test_is_win(self, g_diag_upper_left_win):
        assert g_diag_upper_left_win.is_win() == True

@pytest.fixture()
def g_diag_upper_right_win():
    g = play_game()
    g.move('11')
    g.move('13')
    g.move('21')
    g.move('22')
    g.move('33')
    g.move('31')
    return g

class Test_diag_upper_right_win(object):
    def test_outcome(self, g_diag_upper_right_win):
        assert g_diag_upper_right_win.outcome == "O win"

    def test_is_win(self, g_diag_upper_right_win):
        assert g_diag_upper_right_win.is_win() == True