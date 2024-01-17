from math import inf

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
    
    # #the heuristic evaluation functions
    def heuristic3(self, piece):
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
    

    def heuristic2(self, maximizing_player):
        board = self.board
        values_matrix = [
            [3, 4, 5, 7, 5, 4, 3],
            [4, 6, 8, 10, 8, 6, 4],
            [5, 8, 11, 13, 11, 8, 5],
            [5, 8, 11, 13, 11, 8, 5],
            [4, 6, 8, 10, 8, 6, 4],
            [3, 4, 5, 7, 5, 4, 3]
        ]

        HV = 0  # Heuristic Value

        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] == maximizing_player:
                    HV += values_matrix[row][col]

        return HV
    
    def heuristic1(self, maximizing_player):
        HV = 0  # Heuristic Value
        board = self
        # Feature 1: Four chessmen connected
        if self.win(maximizing_player):
            return inf

        # Feature 2: Three chessmen connected
        feature2_val = evaluate_feature2(board, maximizing_player)
        if feature2_val == inf:
            return inf
        HV += feature2_val

        # Feature 3: Two chessmen connected
        HV += evaluate_feature3(board, maximizing_player)

        # Feature 4: Lone chessman
        HV += evaluate_feature4(board, maximizing_player)

        return HV
    

def evaluate_feature2(board, maximizing_player):
    inf = float('inf')

    def check_window(window):
        if window.count(maximizing_player) == 3 and window.count(0) == 1:
            return inf  # Immediate win
        elif window.count(maximizing_player) == 2 and window.count(0) == 1:
            # A move can only be made on one of the immediately adjacent columns
            return 900000
        elif window.count(maximizing_player) == 1 and window.count(0) == 2:
            # A same chessman can be found a square away from two connected men
            return 900000
        elif window.count(maximizing_player) == 1 and window.count(0) == 1:
            # A move can be made on either immediately adjacent columns
            return 50000
        else:
            return 0

    feature2_val = 0

    # Check horizontally
    for row in range(board.rows):
        for col in range(board.cols - 2):
            window = [board.board[row][col + i] for i in range(3)]
            feature2_val += check_window(window)

    # Check vertically
    for row in range(board.rows - 2):
        for col in range(board.cols):
            window = [board.board[row + i][col] for i in range(3)]
            feature2_val += check_window(window)

    # Check diagonally (bottom-left to top-right)
    for row in range(2, board.rows):
        for col in range(board.cols - 2):
            window = [board.board[row - i][col + i] for i in range(3)]
            feature2_val += check_window(window)

    # Check diagonally (top-left to bottom-right)
    for row in range(board.rows - 2):
        for col in range(board.cols - 2):
            window = [board.board[row + i][col + i] for i in range(3)]
            feature2_val += check_window(window)

    return feature2_val


def evaluate_feature3(board, maximizing_player):
    feature3_val = 0

    def check_window(window):
        available_squares = window.count(0)
        if window.count(maximizing_player) == 1 and available_squares > 0:
            if available_squares == 5:
                return 40000
            elif available_squares == 4:
                return 30000
            elif available_squares == 3:
                return 20000
            elif available_squares == 2:
                return 10000
        return 0

    # Check horizontally
    for row in range(board.rows):
        for col in range(board.cols - 1):
            window = [board.board[row][col + i] for i in range(2)]
            feature3_val += check_window(window)

    # Check vertically
    for row in range(board.rows - 1):
        for col in range(board.cols):
            window = [board.board[row + i][col] for i in range(2)]
            feature3_val += check_window(window)

    # Check diagonally (bottom-left to top-right)
    for row in range(1, board.rows):
        for col in range(board.cols - 1):
            window = [board.board[row - i][col + i] for i in range(2)]
            feature3_val += check_window(window)

    # Check diagonally (top-left to bottom-right)
    for row in range(board.rows - 1):
        for col in range(board.cols - 1):
            window = [board.board[row + i][col + i] for i in range(2)]
            feature3_val += check_window(window)

    return feature3_val


def evaluate_feature4(board, maximizing_player):
    feature4_val = 0
    for col in range(board.cols):
        for row in range(board.rows - 1, -1, -1):
            if board.board[row][col] == maximizing_player and not any(board.board[i][col] == maximizing_player for i in range(row + 1, board.rows)):
                # A chessman that is not connected to another same chessman
                if col == 3:  # Middle column
                    feature4_val += 200
                elif col in [2, 6]:  # Columns close to the middle
                    feature4_val += 120
                elif col in [1, 7]:  # Outer columns
                    feature4_val += 40
                break  # Only consider the lowest chessman in the column

    return feature4_val