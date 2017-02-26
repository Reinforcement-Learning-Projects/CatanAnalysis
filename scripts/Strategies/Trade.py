from settings import printv

class Trade:
    
    type = None
        # 'none' - never trades with anyone

    playerId = None
    Board = None
    players = None

    def __init__( self, type, playerId, board, players ):
        self.type = type
        self.playerId = playerId
        self.Board = board
        self.players = players

    def go( self ):
        if self.type == 'none':
            self.none()
    
    def none( self ):
        printv( '    none' )