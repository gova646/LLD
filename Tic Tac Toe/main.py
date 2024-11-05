from game import Game
from player import Player

boardSize = int(input('Enter board Size'))

player1 = input('Enter player1 Name')
player1Symbol = input('Enter symbol of Player1')
player2 = input('Enter player2 Name')
player2Symbol = input('Enter symbol of Player2')

player1 = Player(player1, player1Symbol)
player2 = Player(player2, player2Symbol)

game = Game(boardSize)
game.intializeBoard()
def getNextPlayer(currentPlayer):
    if currentPlayer == player1:
        return player2
    return player1

gamePlay = True
currentPlayer = player1
while gamePlay:
    game.displayBoard()
    print(currentPlayer.name + ' Move')
    row = int(input('Enter the row'))
    column = int(input('Enter the column'))
    if game.checkIfValidMove(row, column):
        print('Invalid Move')
        continue
    winStatus = game.makeMove(currentPlayer, row,column)
    if winStatus:
        print(currentPlayer.name + 'Won the match')
        currentPlayer.gamesPlayed+=1
        currentPlayer.gamesWon += 1
        otherPlayer = getNextPlayer(currentPlayer)
        otherPlayer.gamesPlayed+=1
        otherPlayer.gamesLost +=1
        moreGame = input('Do you want to continue')
        if moreGame != 'yes':
            gamePlay = False
            continue
        game.intializeBoard()
    currentPlayer = getNextPlayer(currentPlayer)





