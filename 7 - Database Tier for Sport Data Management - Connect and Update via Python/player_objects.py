# Business tier for the Players' data manager program

class Player:

    def __init__(self, name:str, wins:int=0, losses:int=0, ties:int=0, id:int=0):

        self.name = name
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.id = id


    @property
    def games(self):

        games = self.wins + self.losses + self.ties
        return games


def main():

    player = Player("Joel")
    print(player.name, player.id, player.wins, player.games)    


if __name__ == "__main__":
    main()
