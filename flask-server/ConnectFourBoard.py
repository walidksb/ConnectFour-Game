from math import inf
import random

class ConnectFourBoard:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = [[0] * cols for _ in range(rows)]
    
    #a simple draw of the board
    def drawBoard(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(f"| {self.board[row][col]}", end=" ")
            print("|")
            print("-" * (4 * self.cols + 1))
    
    #returns the possible moves "columns"
    def getPossibleMoves(self):
        moves = []
        for col in range(self.cols):
            if self.board[0][col] == 0:
                moves.append(col)
        # print(moves)        
        return moves
    
    #make the move on the board
    def makeMove(self, row, col, piece):
        self.board[row][col] = piece

    #check the 4 possible win conditions
    def win(self, piece):
        # Check for a win in rows
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row][col + i] == piece for i in range(4)):
                    return True

        # Check for a win in columns
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if all(self.board[row + i][col] == piece for i in range(4)):
                    return True

        # Check for a win in diagonals (bottom-left to top-right)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row - i][col + i] == piece for i in range(4)):
                    return True

        # Check for a win in diagonals (top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == piece for i in range(4)):
                    return True
        return False
    
    #check if the game is over with a win or no more possible moves
    def gameOver(self):
        return self.win(1) or self.win(2) or not self.getPossibleMoves()
    
    #the heuristic evaluation functions
    def heuristic1(self, piece):
        # Simple heuristic: count the number of pieces in a row for the given piece
        count = 0
        for row in range(self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row][col + i] for i in range(4)]
                count += window.count(piece)

        for row in range(self.rows - 3):
            for col in range(self.cols):
                window = [self.board[row + i][col] for i in range(4)]
                count += window.count(piece)

        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row - i][col + i] for i in range(4)]
                count += window.count(piece)

        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                window = [self.board[row + i][col + i] for i in range(4)]
                count += window.count(piece)
        return count
    
    
    
    def heuristic3(self, piece):
        opponent_piece = 3 - piece  # Assuming pieces are represented as 1 and 2
        
        my_material = 0
        opponent_material = 0

        # Helper function to calculate material based on contiguous lines
        def calculate_material(window):
            material = 0
            count = window.count(piece)
            if count > 0:
                material += 0.1 * count
            count = window.count(piece)
            if count > 1:
                material += 0.3 * count
            count = window.count(piece)
            if count > 2:
                material += 0.9 * count
            return material

        # Check for material in rows
        for row in range(self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row][col + i] for i in range(4)]
                my_material += calculate_material(window)

        # Check for material in columns
        for row in range(self.rows - 3):
            for col in range(self.cols):
                window = [self.board[row + i][col] for i in range(4)]
                my_material += calculate_material(window)

        # Check for material in diagonals (bottom-left to top-right)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row - i][col + i] for i in range(4)]
                my_material += calculate_material(window)

        # Check for material in diagonals (top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                window = [self.board[row + i][col + i] for i in range(4)]
                my_material += calculate_material(window)

        # Calculate opponent's material using the same logic
        for row in range(self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row][col + i] for i in range(4)]
                opponent_material += calculate_material(window)

        for row in range(self.rows - 3):
            for col in range(self.cols):
                window = [self.board[row + i][col] for i in range(4)]
                opponent_material += calculate_material(window)

        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row - i][col + i] for i in range(4)]
                opponent_material += calculate_material(window)

        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                window = [self.board[row + i][col + i] for i in range(4)]
                opponent_material += calculate_material(window)

        # Return the difference between my material and opponent's material
        return my_material - opponent_material



    #a heuristic that calculates the number of occurance of a player in the four sides
    #and tries to block him in case of winning 
    def heuristic2(self, piece):
    # this heuristic is based on strategic positions on the board
    # the center is the most important position
    # the corners are the second most important position
    # the sides are the least important position
    
        if self.win(piece):
            return 100000
        if self.win(3 - piece):
            return -100000
        
        score = 0
        score += 4 * self.evaluateCenterControl(piece)
        score += 1 * self.evaluateCornerControl(piece)  # Give corners higher weight
        score += 0.5 * self.evaluateSideControl(piece)  # Give sides lower weight
        score += self.checkDoubleSideWin(piece)
        score += 20 * self.checkBlockingMove(piece)
        score += 1000 * self.checkWinningMove(piece)

        return score
    def checkDoubleSideWin(self, piece):
        opponent_piece = 3 - piece

        # Check for potential double-sided wins in rows
        for row in range(self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row][col + i] for i in range(4)]
                if window[1] == opponent_piece and window[2] == opponent_piece and window.count(0) == 2:
                    return -1000  # Penalize the opponent for potential double-sided win

        # Check for potential double-sided wins in diagonals (bottom-left to top-right)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row - i][col + i] for i in range(4)]
                if window[1] == opponent_piece and window[2] == opponent_piece and window.count(0) == 2:
                    return -1000

        # Check for potential double-sided wins in diagonals (top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                window = [self.board[row + i][col + i] for i in range(4)]
                if window[1] == opponent_piece and window[2] == opponent_piece and window.count(0) == 2:
                    return -1000

        return 0

    def evaluateCenterControl(self, piece):
        center_col = self.cols // 2
        center_count = 0

        for row in range(self.rows):
            if self.board[row][center_col] == piece:
                center_count += 1

        return center_count
    
    def evaluateCornerControl(self, piece):
        corner_count = 0

        if self.board[0][0] == piece:
            corner_count += 1
        if self.board[0][self.cols - 1] == piece:
            corner_count += 1
        if self.board[self.rows - 1][0] == piece:
            corner_count += 1
        if self.board[self.rows - 1][self.cols - 1] == piece:
            corner_count += 1

        return corner_count
    
    def evaluateSideControl(self, piece):
        side_count = 0

        for row in range(self.rows):
            if self.board[row][0] == piece:
                side_count += 1
            if self.board[row][self.cols - 1] == piece:
                side_count += 1

        for col in range(1, self.cols - 1):
            if self.board[0][col] == piece:
                side_count += 1
            if self.board[self.rows - 1][col] == piece:
                side_count += 1

        return side_count

    def checkBlockingMove(self, piece):
        # Check for potential blocking moves in rows
        for row in range(self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row][col + i] for i in range(4)]
                if window.count(piece) == 3 and window.count(0) == 1:
                    return 50  # Encourage blocking opponent's winning move

        # Check for potential blocking moves in diagonals (bottom-left to top-right)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row - i][col + i] for i in range(4)]
                if window.count(piece) == 3 and window.count(0) == 1:
                    return 50

        # Check for potential blocking moves in diagonals (top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                window = [self.board[row + i][col + i] for i in range(4)]
                if window.count(piece) == 3 and window.count(0) == 1:
                    return 50

        # Check for potential blocking moves in columns
        for col in range(self.cols):
            for row in range(self.rows - 3):
                window = [self.board[row + i][col] for i in range(4)]
                if window.count(piece) == 3 and window.count(0) == 1:
                    return 50

        return 0

    def checkWinningMove(self, piece):
        # Check for potential winning moves in rows
        for row in range(self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row][col + i] for i in range(4)]
                if window.count(piece) == 3 and window.count(0) == 1:
                    return 100  # Encourage making winning move

        # Check for potential winning moves in diagonals (bottom-left to top-right)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row - i][col + i] for i in range(4)]
                if window.count(piece) == 3 and window.count(0) == 1:
                    return 100

        # Check for potential winning moves in diagonals (top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                window = [self.board[row + i][col + i] for i in range(4)]
                if window.count(piece) == 3 and window.count(0) == 1:
                    return 100

        # Check for potential winning moves in columns
        for col in range(self.cols):
            for row in range(self.rows - 3):
                window = [self.board[row + i][col] for i in range(4)]
                if window.count(piece) == 3 and window.count(0) == 1:
                    return 100

        return 0