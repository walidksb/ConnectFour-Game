import random
from math import inf
from ConnectFourBoard import ConnectFourBoard

class Play:
    def __init__(self, board):
        self.board = board
        self.game_id = None

    #ai bot 1
    def AIbot1(self):
        depth = 5
        _,best_move = self.minimaxAlphaBetaPruning(self.board,depth, True, float('-inf'), float('inf'),1)
        return best_move
    
    #ai bot 2 is the same as ai bot 1 but with a different heuristic
    def AIbot2(self):
        depth = 5
        _,best_move = self.minimaxAlphaBetaPruning(self.board,depth, True, float('-inf'), float('inf'),2)
        return best_move
            
    def minimaxAlphaBetaPruning(self,board, depth, maximizingPlayer, alpha, beta,heuristic):
        if depth == 0 or board.gameOver():
            if(heuristic==1):
                return board.heuristic2(2),None
            else:
                return board.heuristic1(2),None

        if maximizingPlayer:
            max_eval = float('-inf')
            best_move = None
            for move in board.getPossibleMoves():
                row = max([r for r in range(board.rows) if board.board[r][move] == 0])
                board.makeMove(row, move, 2)
                eval,_ = self.minimaxAlphaBetaPruning(board,depth - 1, False, alpha, beta,heuristic)
                board.makeMove(row, move, 0)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                # max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in board.getPossibleMoves():
                row = max([r for r in range(board.rows) if board.board[r][move] == 0])
                board.makeMove(row, move, 1)
                eval,_ = self.minimaxAlphaBetaPruning(board,depth - 1, True, alpha, beta,heuristic)
                board.makeMove(row, move, 0)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                # min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move
