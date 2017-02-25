# setup Phase
# Turn phase
#  Roll
#   Collect/Steal and discard half over 7
#  Trade
#  Build and Cards
# ->Turn phase next player
from random import randint

class Phases:
    
    players = []
    Board = None
    whosTurn = 0

    #
    fakeTurnLimit = 20
    fakeTurnLimitCount = 1
    #

    def __init__( self, players, board ):
        self.players = players
        self.Board = board
        self.setup()
        self.turn( 0 )
    
    # first player to last player then last player to first player building
    def setup( self ):
        for p in self.players:
            p.do( 'setup' )
        for p in reversed(self.players):
            p.do( 'setup' )

    def turn( self, i ):
        roll = self.rollDice()
        print str(i) + ' rolled a ' + str(roll)
        if roll is 7:
            self.allPlayersDo( 'discard' )
            self.players[i].do( 'rob' )
        else:
            self.deliverCards( roll )
        
        self.players[i].do( 'trade' )
        self.players[i].do( 'build' )

        if self.players[i].points >= 10:
            print( self.players[i].playerCode + ' won!' )
        else:
            if self.fakeTurnLimitCount < self.fakeTurnLimit:
                self.fakeTurnLimitCount += 1
                self.turn( (i+1) % len(self.players) )
        
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
                    if pos.playerId is not None:
                        self.players[ pos.playerId ].addCard( hex.resource )
        
    