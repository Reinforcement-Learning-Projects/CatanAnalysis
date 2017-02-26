from settings import printv

from Strategy import Strategy

class Player:
    playerId = None
    cards = None
    points = None
    Strategy = None

    def __init__( self, id, board, players ):
        self.playerId = id
        self.cards = []
        self.points = 0
        self.Strategy = Strategy( self.playerId, board, players )

    def do( self, do, witha=None ):
        printv( str(self.playerId) + ' ' + do )
        if do == 'collect':
            self.collect( witha )
        else:
            self.Strategy.play( do )

    def addCard( self, card ):
        self.cards.append( card )

    def showCards( self ):
        print( "Player " + str(self.playerId) + "'s Cards: " )
        print( "    Grain: " + str(self.cards.count( 'grain' )) )
        print( "    Sheep: " + str(self.cards.count( 'sheep' )) )
        print( "     Wood: " + str(self.cards.count( 'wood' )) )
        print( "    Brick: " + str(self.cards.count( 'brick' )) )
        print( "      Ore: " + str(self.cards.count( 'ore' )) )
