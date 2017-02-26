from settings import printv

class Build:
    
    type = None
        # 'best' - builds something that leaves the players total points highest
    
    playerId = None
    Board = None
    players = None

    def __init__( self, type, playerId, board, players ):
        self.type = type
        self.playerId = playerId
        self.Board = board
        self.players = players

    def go( self ):
        if self.type == 'best':
            self.best()
    
    def best( self ):
        printv( '    best' )
