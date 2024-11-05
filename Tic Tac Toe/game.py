class Game:
    def __init__(self, boardSize) -> None:
        self.boardSize = boardSize
    
    def intializeBoard(self):
        self.board = [['#' for j in range(self.boardSize)] for i in range(self.boardSize)]

    def displayBoard(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                print(self.board[i][j], end='\t')
            print('')
    
    def checkIfValidMove(self, row, column):
        if row >= self.boardSize or column >= self.boardSize:
            return True
        return False

    def makeMove(self, currentPlayer, row , column):
        self.board[row][column] = currentPlayer.symbol
        return self.checkIfWinner(currentPlayer, row, column)
    
    def checkIfWinner(self, currentPlayer,row, column):
        rowCheck = columnCheck = forwardDiagonalCheck = backDiagonalCheck = True
        for i in range(self.boardSize):
            if self.board[row][i] != currentPlayer.symbol:
                rowCheck =  False
            if self.board[i][column] != currentPlayer.symbol:
                columnCheck =  False
        if row != column:
            forwardDiagonalCheck =backDiagonalCheck = False
        else:
            #forwad and back Diagonal check
            for i in range(self.boardSize):
                if self.board[i][i] != currentPlayer.symbol:
                    forwardDiagonalCheck = False
                if self.board[i][self.boardSize-1-i] != currentPlayer.symbol:
                    backDiagonalCheck = False
        return rowCheck or columnCheck or forwardDiagonalCheck or backDiagonalCheck
        

                    

