import enum

class GridPosition(enum.Enum):
    EMPTY = 0
    YELLOW = 1
    RED = 2

class Grid:
    def __init__(self, rows, columns):
        self._rows = rows#Using _ to declare private
        self._columns = columns
        self._grid = None
        self.initGrid()
    def initGrid(self):
        self.grid = [[GridPosition.EMPTY for _ in range(self.columns)] for _ in range(self.rows)]
    def getGrid(self):
        return self._grid
    def getColumnCount(self):
        return self._columns
    def getRowCount(self):
        return self._rows
    def placePiece(self, column, piece):
        if column < 0 or column > self.getColumnCount:
            raise ValueError('Invalid Column Number')
        if piece == GridPosition.EMPTY:
            return ValueError('Invalid piece')
        for row in range(0, self.getRowCount, 1):
            if self._grid[row][column] == GridPosition.EMPTY:
                self._grid[row][column] = piece
    def checkWin(self, connectN, row, col, piece):

        #check horizontal
        count = 0
        for c in range(self.getColumnCount):
            if self._grid[row][c] == piece:
                count += 1
            else:
                count = 0
        if count == connectN:
            return True
        #check vertical
        count = 0
        for c in range(self.getRowCount):
            if self._grid[col][c] == piece:
                count += 1
            else:
                count = 0
        if count == connectN:
            return True
        # Check diagonal
        count = 0
        for r in range(self._rows):
            c = row + col - r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check anti-diagonal
        count = 0
        for r in range(self._rows):
            c = col - row + r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        return False

class Player:
    def __init__(self, name, pieceColor):
        self._name = name
        self._pieceColor = pieceColor
    def getName(self):
        return self._name
    def getPieceColor(self):
        return self._pieceColor

class Game:
    def __init__(self, grid, connectN, targetScore):
        self._grid = grid
        self._connectN = connectN
        self._targetScore = targetScore
        
        self.players = [
            Player('Player 1', GridPosition.YELLOW),
            Player('Player 2', GridPosition.RED)
        ]

        for player in self.players:
            self._score[player.getName()] = 0
        
    def printBoard(self):
        pass