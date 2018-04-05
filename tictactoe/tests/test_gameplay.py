import pytest
from tictactoe import *

#####
#
# Initialization tests
#
####

@pytest.fixture()
def g0():
    g = play_game()
    return g

class Test_initial_values(object):
    def test_type(self, g0):
        assert isinstance(g0, tictactoeboard)
        
    def test_board(self, g0):
        assert g0.board == {'11': ' ',
                            '12': ' ',
                            '13': ' ',
                            '21': ' ',
                            '22': ' ',
                            '23': ' ',
                            '31': ' ',
                            '32': ' ',
                            '33': ' '}

    def test_current_move(self, g0):
        assert g0.current_move == 'X'  

    def test_previous_move(self, g0):
        assert g0.previous_move == None

    def test_history(self, g0):
        assert g0.history == []

    def test_outcome(self, g0):
        assert g0.outcome == None

    def test_available_moves(self, g0):
        assert g0.available_moves() == ['11', '12', '13', '21', '22', '23', '31', '32', '33']

    def test_are_moves_left(self, g0):
        assert g0.are_moves_left() == True

    def test_is_win(self, g0):
        assert g0.is_win() == False

    def test_print(self, g0, capsys):
        print(g0)
        out, err = capsys.readouterr()
        assert out == '   |   |   \n-----------\n   |   |   \n-----------\n   |   |   ' + '\n'

#####
#
# First move tests
#
####

def test_error_invalid_position(g0):
    with pytest.raises(ValueError) as excinfo:
        g0.move("44")
    assert 'Invalid position' in str(excinfo.value)

@pytest.fixture()
def g1():
    g = play_game()
    g.move('22')
    return g

class Test_first_move(object):
    def test_board(self, g1):
        assert g1.board == {'11': ' ',
                            '12': ' ',
                            '13': ' ',
                            '21': ' ',
                            '22': 'X',
                            '23': ' ',
                            '31': ' ',
                            '32': ' ',
                            '33': ' '}

    def test_current_move(self, g1):
        assert g1.current_move == 'O'  

    def test_previous_move(self, g1):
        assert g1.previous_move == 'X'

    def test_history(self, g1):
        assert g1.history == [{'11': ' ',
                               '12': ' ',
                               '13': ' ',
                               '21': ' ',
                               '22': 'X',
                               '23': ' ',
                               '31': ' ',
                               '32': ' ',
                               '33': ' '}]

    def test_outcome(self, g1):
        assert g1.outcome == None

    def test_available_moves(self, g1):
        assert g1.available_moves() == ['11', '12', '13', '21', '23', '31', '32', '33']

    def test_are_moves_left(self, g1):
        assert g1.are_moves_left() == True

    def test_is_win(self, g1):
        assert g1.is_win() == False

    def test_print(self, g1, capsys):
        print(g1)
        out, err = capsys.readouterr()
        assert out == '   |   |   \n-----------\n   | X |   \n-----------\n   |   |   ' + '\n'
        
#####
#
# Second move tests
#
####

def test_error_piece_already_there(g1):
    with pytest.raises(ValueError) as excinfo:
        g1.move("22")
    assert 'Piece already at that position' in str(excinfo.value)

@pytest.fixture()
def g2():
    g = play_game()
    g.move('22')
    g.move('11')
    return g

class Test_second_move(object):
    def test_board(self, g2):
        assert g2.board == {'11': 'O',
                            '12': ' ',
                            '13': ' ',
                            '21': ' ',
                            '22': 'X',
                            '23': ' ',
                            '31': ' ',
                            '32': ' ',
                            '33': ' '}

    def test_current_move(self, g2):
        assert g2.current_move == 'X'

    def test_previous_move(self, g2):
        assert g2.previous_move == 'O'

    def test_history(self, g2):
        assert g2.history == [{'11': ' ',
                               '12': ' ',
                               '13': ' ',
                               '21': ' ',
                               '22': 'X',
                               '23': ' ',
                               '31': ' ',
                               '32': ' ',
                               '33': ' '},
                              {'11': 'O',
                               '12': ' ',
                               '13': ' ',
                               '21': ' ',
                               '22': 'X',
                               '23': ' ',
                               '31': ' ',
                               '32': ' ',
                               '33': ' '}]

    def test_outcome(self, g2):
        assert g2.outcome == None

    def test_available_moves(self, g2):
        assert g2.available_moves() == ['12', '13', '21', '23', '31', '32', '33']

    def test_are_moves_left(self, g2):
        assert g2.are_moves_left() == True

    def test_is_win(self, g2):
        assert g2.is_win() == False

    def test_print(self, g2, capsys):
        print(g2)
        out, err = capsys.readouterr()
        assert out == ' O |   |   \n-----------\n   | X |   \n-----------\n   |   |   ' + '\n'

#####
#
# Game finished tests
#
####

@pytest.fixture()
def g3():
    g = play_game()
    g.move('11')
    g.move('21')
    g.move('12')
    g.move('22')
    g.move('13')
    return g

class Test_game_finish(object):
    def test_board(self, g3):
        assert g3.board == {'11': 'X',
                            '12': 'X',
                            '13': 'X',
                            '21': 'O',
                            '22': 'O',
                            '23': ' ',
                            '31': ' ',
                            '32': ' ',
                            '33': ' '}

    def test_current_move(self, g3):
        assert g3.current_move == 'O'

    def test_previous_move(self, g3):
        assert g3.previous_move == 'X'

    def test_history(self, g3):
        assert g3.history == [{'11': 'X',
                               '12': ' ',
                               '13': ' ',
                               '21': ' ',
                               '22': ' ',
                               '23': ' ',
                               '31': ' ',
                               '32': ' ',
                               '33': ' '},
                              {'11': 'X',
                               '12': ' ',
                               '13': ' ',
                               '21': 'O',
                               '22': ' ',
                               '23': ' ',
                               '31': ' ',
                               '32': ' ',
                               '33': ' '},
                              {'11': 'X',
                               '12': 'X',
                               '13': ' ',
                               '21': 'O',
                               '22': ' ',
                               '23': ' ',
                               '31': ' ',
                               '32': ' ',
                               '33': ' '},
                              {'11': 'X',
                               '12': 'X',
                               '13': ' ',
                               '21': 'O',
                               '22': 'O',
                               '23': ' ',
                               '31': ' ',
                               '32': ' ',
                               '33': ' '},
                              {'11': 'X',
                               '12': 'X',
                               '13': 'X',
                               '21': 'O',
                               '22': 'O',
                               '23': ' ',
                               '31': ' ',
                               '32': ' ',
                               '33': ' '}]

    def test_outcome(self, g3):
        assert g3.outcome == "X win"

    def test_available_moves(self, g3):
        assert g3.available_moves() == ['23', '31', '32', '33']

    def test_are_moves_left(self, g3):
        assert g3.are_moves_left() == True

    def test_is_win(self, g3):
        assert g3.is_win() == True

    def test_print(self, g3, capsys):
        print(g3)
        out, err = capsys.readouterr()
        assert out == ' X | X | X \n-----------\n O | O |   \n-----------\n   |   |   ' + '\n'

    def test_error_board_finished(self, g3):
        with pytest.raises(ValueError) as excinfo:
            g3.move("33")
        assert 'Board is finished' in str(excinfo.value)