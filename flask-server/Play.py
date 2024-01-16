import random
from math import inf
from ConnectFourBoard import ConnectFourBoard

class Play:
    def __init__(self, board):
        self.board = board
        self.game_id = None

    #ai bot 1
    def AIbot1(self):
        depth = 4
        _,best_move = self.minimaxAlphaBetaPruning(self.board,depth, True, float('-inf'), float('inf'),1)
        return best_move
    
    #ai bot 2 is the same as ai bot 1 but with a different heuristic
    def AIbot2(self):
        depth = 4
        _,best_move = self.minimaxAlphaBetaPruning(self.board,depth, True, float('-inf'), float('inf'),2)
        return best_move
            
    def minimaxAlphaBetaPruning(self,board, depth, maximizingPlayer, alpha, beta,heuristic):
        if depth == 0 or board.gameOver():
            if(heuristic==1):
                return board.heuristic3(2),None
            else:
                return board.heuristic2(2),None

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









# def minimaxAlphaBetaPruning(
#         self, board, depth, alpha, beta, maximizingPlayer, heuristic_function
#     ):
#         if depth == 0 or board.gameOver():
#             return heuristic_function(board, 2), None

#         possible_moves = board.getPossibleMoves()

#         if maximizingPlayer:
#             maxEval = float("-inf")
#             bestMove = None
#             for col in possible_moves:
#                 row = max([r for r in range(board.rows) if board.board[r][col] == 0])
#                 board.makeMove(row, col, 2)
#                 eval, _ = self.minimaxAlphaBetaPruning(
#                     board, depth - 1, alpha, beta, False, heuristic_function
#                 )
#                 board.makeMove(row, col, 0)
#                 if eval > maxEval:
#                     maxEval = eval
#                     bestMove = (row, col)
#                 alpha = max(alpha, eval)
#                 if beta <= alpha:
#                     break
#             return maxEval, bestMove
#         else:
#             minEval = float("inf")
#             bestMove = None
#             for col in possible_moves:
#                 row = max([r for r in range(board.rows) if board.board[r][col] == 0])
#                 board.makeMove(row, col, 1)
#                 eval, _ = self.minimaxAlphaBetaPruning(
#                     board, depth - 1, alpha, beta, True, heuristic_function
#                 )
#                 board.makeMove(row, col, 0)
#                 if eval < minEval:
#                     minEval = eval
#                     bestMove = (row, col)
#                 beta = min(beta, eval)
#                 if beta <= alpha:
#                     break
#             return minEval, bestMove

#  def minimaxAlphaBetaPruning(self, board, depth, alpha, beta,maximizingPlayer,heuristic=1):
#         if depth == 0 or board.gameOver():
#             if heuristic == 1:
#                 return board.heuristic1(2)
#             else :
#                 return board.heuristic2(2)

#         possibleMoves = board.getPossibleMoves()
#         if maximizingPlayer:
#             maxEval = -inf
#             bestMove = None
#             for move in possibleMoves:
#                 newBoard = ConnectFourBoard()
#                 newBoard.board = [row[:] for row in board.board]
#                 row = self.findLowestEmptyRow(move[1])  # Extract the column from the tuple
#                 newBoard.makeMove(row, move[1], 2)  # Extract the column from the tuple
#                 eval, _ = self.minimaxAlphaBetaPruning(newBoard, depth - 1, alpha, beta, False,heuristic)
#                 if eval > maxEval:
#                     maxEval = eval
#                     bestMove = move[1]  # Extract the column from the tuple
#                 alpha = max(alpha, eval)
#                 if beta <= alpha:
#                     break
#             return maxEval
#         else:
#             minEval = inf
#             bestMove = None
#             for move in possibleMoves:
#                 newBoard = ConnectFourBoard()
#                 newBoard.board = [row[:] for row in board.board]
#                 row = self.findLowestEmptyRow(move[1])  # Extract the column from the tuple
#                 newBoard.makeMove(row, move[1], 1)  # Extract the column from the tuple
#                 eval, _ = self.minimaxAlphaBetaPruning(newBoard, depth - 1, alpha, beta,True,heuristic)
#                 if eval < minEval:
#                     minEval = eval
#                     bestMove = move[1]  # Extract the column from the tuple
#                 beta = min(beta, eval)
#                 if beta <= alpha:
#                     break
#             return minEval