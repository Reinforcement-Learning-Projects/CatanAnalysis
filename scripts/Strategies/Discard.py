from settings import printv

from random import randint
import math

class Discard:
    
    type = None
        # 'random' - randomly discard floor(half) cards when over 8 cards when 7 rolls

    playerId = None
    Board = None
    players = None

    def __init__( self, type, playerId, board, players ):
        self.type = type
        self.playerId = playerId
        self.Board = board
        self.players = players

    def go( self ):
        if self.type == 'random':
            self.random()
    
    # randomly discard floor(half) cards when over 8 cards when 7 rolls
    def random( self ):
        curCardLen = len( self.players[self.playerId].cards )
        newCardLen = curCardLen
        if curCardLen > 7:
            newCardLen = math.ceil( newCardLen / 2 )
            printv( '    ' + str(self.playerId) + ' is discarding ' + str(int(curCardLen - newCardLen)) +' cards' )

        while curCardLen > newCardLen:
            ri = randint( 0, curCardLen - 1 )
            self.players[self.playerId].cards.pop( ri )
            curCardLen = len( self.players[self.playerId].cards )
            
            
        