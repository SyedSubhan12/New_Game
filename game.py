import time
from Player import HumanPlayer,RandomComputerPlayer

class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]  # Initialize the board
        self.current_winner = None  # Track the current winner

    def print_board(self):
        # This function prints the current state of the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_nums():
        # This function prints the board numbers
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')

    def available_moves(self):
        # This function returns the available moves
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        # This function checks if there are empty squares left
        return " " in self.board
    
    def num_empty_square(self):
        # This function returns the number of empty squares
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # This function makes a move on the board
        if self.board[square] ==' ':
            self.board[square] = letter  # Corrected the assignment operator
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # This function checks if there is a winner
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
             return True
        
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
             return True
        
        if square  % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False    
    
def play(game, x_player, o_player, print_game=True):
    # This function starts the game
    if print_game:
        game.print_board_nums()

    letter = 'X'    

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' make a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')  # Added a space before 'wins!'
                return letter     
            letter = 'O' if letter =='X' else 'X'
        time.sleep(0.8)   

    if print_game and not game.current_winner:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True )
