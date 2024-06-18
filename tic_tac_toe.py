# tic_tac_toe.py

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9  # Initialize the board with empty spaces
        self.current_player = 'X'  # X always starts first
        self.winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]

    def make_move(self, position):
        """Make a move at the given position."""
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        """Check if there's a winner or a draw."""
        for combo in self.winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]) and (self.board[combo[0]] != ' '):
                return self.board[combo[0]]
        if ' ' not in self.board:
            return 'draw'
        return None

    def reset_board(self):
        """Reset the board for a new game."""
        self.board = [' '] * 9
        self.current_player = 'X'

    def minimax(self, depth, is_maximizing):
        """Minimax algorithm to find the best move."""
        winner = self.check_winner()
        if winner == 'X':
            return -10 + depth, None
        elif winner == 'O':
            return 10 - depth, None
        elif winner == 'draw':
            return 0, None

        if is_maximizing:
            best_score = -float('inf')
            best_move = None
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    score, _ = self.minimax(depth + 1, False)
                    self.board[i] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = i
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    score, _ = self.minimax(depth + 1, True)
                    self.board[i] = ' '
                    if score < best_score:
                        best_score = score
                        best_move = i
            return best_score, best_move

    def ai_move(self):
        """Make the best move for the AI."""
        _, best_move = self.minimax(0, True)
        if best_move is not None:
            self.make_move(best_move)
