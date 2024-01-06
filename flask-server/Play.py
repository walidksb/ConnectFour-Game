import random
from math import inf

class Play:
    def __init__(self, board):
        self.board = board
        self.game_id = None

    #ai bot 1
    def AIbot1(self):
        best_score = float('-inf')
        best_move = None
        for move in self.board.getPossibleMoves():
            self.board.makeMove(0, move, 2)  # Simulate the computer's move
            score = self.minimaxAlphaBetaPruning(0, False, float('-inf'), float('inf'))
            self.board.makeMove(0, move, 0)  # Undo the simulated move

            if score > best_score:
                best_score = score
                best_move = move

        return best_move
    
    #ai bot 2 is the same as ai bot 1 but with a different heuristic
    def AIbot2(self):
        best_score = float('-inf')
        best_move = None
        for move in self.board.getPossibleMoves():
            self.board.makeMove(0, move, 2)  # Simulate the computer's move
            score = self.minimaxAlphaBetaPruning(0, False, float('-inf'), float('inf'),2)
            self.board.makeMove(0, move, 0)  # Undo the simulated move

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimaxAlphaBetaPruning(self, depth, maximizingPlayer, alpha, beta,aibot=1):
        if depth == 3 or self.board.gameOver():
            if(aibot==1):
                return self.board.heuristic1(2)
            return self.board.heuristic2()

        if maximizingPlayer:
            max_eval = float('-inf')
            for move in self.board.getPossibleMoves():
                self.board.makeMove(0, move, 2)
                eval = self.minimaxAlphaBetaPruning(depth + 1, False, alpha, beta)
                self.board.makeMove(0, move, 0)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.board.getPossibleMoves():
                self.board.makeMove(0, move, 1)
                eval = self.minimaxAlphaBetaPruning(depth + 1, True, alpha, beta)
                self.board.makeMove(0, move, 0)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
