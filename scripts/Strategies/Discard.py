from settings import printv

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
    
    def random( self ):
        printv( '    random' )