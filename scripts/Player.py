from Strategy import Strategy

class Player:
    playerCode = "-"
    playerId = None
    playerCodes = [ "@", "#", "$", "%" ]
    cards = []
    points = 0
    Strategy = None

    def __init__( self, id ):
        self.playerId = id
        self.playerCode = self.playerCodes[id]
        self.Strategy = Strategy()

    def do( self, do, witha=None ):
        print( do )
        if do == 'collect':
            self.collect( witha )
        else:
            self.Strategy.play( do )

    def addCard( self, card ):
        self.cards.append( card )