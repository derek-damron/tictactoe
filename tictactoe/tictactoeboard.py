from copy import copy

class tictactoeboard:
    """Current board stored as a dictionary with the following keys:

    ```
    11 | 12 | 13
    ------------
    21 | 22 | 23
    ------------
    31 | 32 | 33
    ```
    
    Where the shorthand is:
    
    - First number is the row starting at the top
    - Second number is the column starting at the left
    
    Possible values are:
    
    - `' '`: No piece
    - `'X'`: X-side piece
    - `'O'`: O-side piece
    """
    
    def __init__(self):
        self.board = {'11': ' ',
                      '12': ' ',
                      '13': ' ',
                      '21': ' ',
                      '22': ' ',
                      '23': ' ',
                      '31': ' ',
                      '32': ' ',
                      '33': ' '}
        self.current_move = 'X'
        self.previous_move = None
        self.history = []
        self.outcome = None
    
    def __str__(self):
        return ' %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s ' % (self.board['11'],
                                                                                             self.board['12'],
                                                                                             self.board['13'],
                                                                                             self.board['21'],
                                                                                             self.board['22'],
                                                                                             self.board['23'],
                                                                                             self.board['31'],
                                                                                             self.board['32'],
                                                                                             self.board['33'])
    
    def move(self, position):
        if self.outcome is not None:
            raise ValueError('Board is finished')
        if position not in self.board.keys():
            raise ValueError('Invalid position')
        if self.board[position] != ' ':
            raise ValueError('Piece already at that position')
        
        self.board[position] = self.current_move
        self.history.append(copy(self.board))
        if self.is_win():
            self.outcome = self.current_move + ' ' + 'win'
        elif not self.are_moves_left():
            self.outcome = 'Draw'
        self.switch_sides()
    
    def available_moves(self):
        return [k for (k,v) in self.board.items() if v == ' ']
        
    def are_moves_left(self):
        if len(self.available_moves()) > 0:
            return True
        else:
            return False
        
    def is_win(self):
        # Row win conditions
        if self.board['11'] != ' ' and \
           self.board['11'] == self.board['12'] and \
           self.board['11'] == self.board['13']:
            return True
        if self.board['21'] != ' ' and \
           self.board['21'] == self.board['22'] and \
           self.board['21'] == self.board['23']:
            return True
        if self.board['31'] != ' ' and \
           self.board['31'] == self.board['32'] and \
           self.board['31'] == self.board['33']:
            return True
        
        # Column win conditions
        if self.board['11'] != ' ' and \
           self.board['11'] == self.board['21'] and \
           self.board['11'] == self.board['31']:
            return True
        if self.board['12'] != ' ' and \
           self.board['12'] == self.board['22'] and \
           self.board['12'] == self.board['32']:
            return True
        if self.board['13'] != ' ' and \
           self.board['13'] == self.board['23'] and \
           self.board['13'] == self.board['33']:
            return True
        
        # Diagonal win conditions
        if self.board['11'] != ' ' and \
           self.board['11'] == self.board['22'] and \
           self.board['11'] == self.board['33']:
            return True
        if self.board['13'] != ' ' and \
           self.board['13'] == self.board['22'] and \
           self.board['13'] == self.board['31']:
            return True
        
        # No win conditions
        return False
        
    def switch_sides(self):
        if self.current_move == 'X':
            self.previous_move = 'X'
            self.current_move = 'O'
        else:
            self.previous_move = 'O'
            self.current_move = 'X'