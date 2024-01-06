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
    
    #a heuristic that calculates the number of occurance of a player in the four sides
    #and tries to block him in case of winning 
    def heuristic2(self):
        score = 0
        for player in [1, 2]:
            for row in range(6):
                for col in range(4):
                    line = [self.board[row][col + i] for i in range(4)]
                    score += self.evaluate_line(line, player)

            for col in range(7):
                for row in range(3):
                    line = [self.board[row + i][col] for i in range(4)]
                    score += self.evaluate_line(line, player)

            for row in range(3, 6):
                for col in range(4):
                    line = [self.board[row - i][col + i] for i in range(4)]
                    score += self.evaluate_line(line, player)

            for row in range(3):
                for col in range(4):
                    line = [self.board[row + i][col + i] for i in range(4)]
                    score += self.evaluate_line(line, player)

        return score

    #a function that gives a score for each case 
    def evaluate_line(self, line, player):
        enemy = 3 - player
        count_player = line.count(player)
        count_enemy = line.count(enemy)

        if count_player == 3:
            return 1000  # the player has a Winning move
        elif count_enemy == 3:
            return -1000  # Block opponent's winning move
        elif count_player == 2 and line.count(0) == 1:
            return 100  # Create a potential winning move
        elif count_enemy == 2 and line.count(0) == 1:
            return -200  # Block opponent's potential winning move 
        elif count_player == 1 and line.count(0) == 2:
            return 10  # Create a potential double move
        elif count_enemy == 1 and line.count(0) == 2:
            return -20  # Block opponent's potential double move 
        else:
            return 0