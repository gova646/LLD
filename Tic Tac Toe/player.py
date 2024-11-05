class Player:
    def __init__(self, name, symbol) -> None:
        self.name = name
        self.symbol = symbol
        self.gamesWon = 0
        self.gamesPlayed = 0
        self.gamesLost = 0
    
    def updateGamesOutcome(self, win):
        self.gamesPlayed+=1
        if win:
            self.gamesWon+=1
        else:
            self.gamesLost+=1