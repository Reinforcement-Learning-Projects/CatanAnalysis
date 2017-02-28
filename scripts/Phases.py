# setup Phase
# Turn phase
#  Roll
#   Collect/Steal and discard half over 7
#  Trade
#  Build and Cards
# ->Turn phase next player
from settings import printv

from random import randint

class Phases:
    
    players = []
    Board = None
    whosTurn = 0

    #
    fakeTurnLimit = 4
    fakeTurnLimitCount = 1
    #

    def __init__( self, players, board ):
        self.players = players
        self.Board = board
        self.setup()
        self.begin()
    
    # first player to last player then last player to first player building
    def setup( self ):
        for p in self.players:
            p.do( 'setup' )
        for p in reversed(self.players):
            p.do( 'setup' )

        self.Board.drawIt()
    
    def begin( self ):
        winner = None
        whoseTurn = 0;
        while winner is None and self.fakeTurnLimitCount <= self.fakeTurnLimit:
            winner = self.turn( whoseTurn )
            whoseTurn = ( whoseTurn + 1 ) % len(self.players)
            self.fakeTurnLimitCount += 1
        
        printv( '' )
        printv( '=======Final========' )
        self.Board.drawIt()
        self.allShowCards()

    def turn( self, i ):
        roll = self.rollDice()
        printv( str(i) + ' rolled a ' + str(roll) )
        if roll is 7:
            self.allPlayersDo( 'discard' )
            self.players[i].do( 'rob' )
        else:
            self.deliverCards( roll )
        
        #self.allShowCards()

        self.players[i].do( 'trade' )
        self.players[i].do( 'build' )

        if self.players[i].points >= 10:
            return self.players[i]
        else:
            return None
        
    def rollDice( self ):
        die1 = randint( 1, 6 )
        die2 = randint( 1, 6 )
        return die1 + die2

    def allPlayersDo( self, do, witha=None ):
        for p in self.players:
            p.do( do, witha )

    def deliverCards( self, roll ):
        for pos in self.Board.positions:
            for hex in pos.hexes:
                if hex.number == roll:
                    if hex.hasRobber == False:
                        if pos.playerId is not None:
                            printv( str(pos.playerId) + ' is getting ' + hex.resource )
                            self.players[ pos.playerId ].addCard( hex.resource )

    def allShowCards( self ):
        for p in self.players:
            p.showCards()
        
    