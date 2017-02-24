
from Player import Player

# Manages the gameplay: rules and turns
class Gameplay:
    Board = None
    players = []

    def __init__( self, Board, numOfPlayers ):
        self.Board = Board
        
        # Make players
        for i in xrange( 0, numOfPlayers ):
            self.__addPlayer(i)

        # If we have 3 or 4, begin
        if len( self.players ) in (3, 4):
            self.begin()
        else:
            print( 'Game Not Started: You need either 3 or 4 players to play.')   

    def __addPlayer( self, id ):
        self.players.append( Player( id ) )
    
    def begin( self ):
        self.__setUpPhase()

    def __setUpPhase( self ):
        print( 'Players choosing starting positions...' )
