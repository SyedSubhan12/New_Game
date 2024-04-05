import math
import random

class Player:
    def __init__(self, letter):
        # Letter is either 'X' or 'O'
        self.letter = letter

    def get_move(self, game):
        # Abstract method, to be overridden by subclasses
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # Choose a random available move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            # Ask the human player for input
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')

        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # If it's the first move, choose a random square
            square = random.choice(game.available_moves())
        else:
            # Otherwise, use minimax algorithm to choose the best move
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            # If the other player has won, return a score based on remaining empty squares
            return {'position': None,
                    'score': 1 * (state.num_empty_square() + 1) if other_player == max_player else -1 * (
                        state.num_empty_square() + 1
                    )}

        elif not state.empty_squares():
            # If it's a tie, return a score of 0
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # Try each possible move
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            # Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
