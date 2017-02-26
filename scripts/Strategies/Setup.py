from settings import printv

from random import randint

class Setup:
    
    type = None
        # 'random' - randomly places initial settlements and roads

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
    
    # Choose the first found valid random position
    # Note: Potential endless loop if other variables are off
    def random( self ):
        spotFound = False
        while not spotFound:
            rand = randint( 0, len(self.Board.positions) - 1 )
            if self.Board.positions[rand].playerId is None:
                
                # Make sure their aren't any adjacent settlements
                # as that would break the distance rule
                noAdjacents = True
                for adj in self.Board.positions[rand].adjPos:
                    if adj.playerId is not None:
                        noAdjacents = False

                if noAdjacents:
                    self.Board.positions[rand].placeBuilding( self.playerId, False )
                    spotFound = True