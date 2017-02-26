from settings import printv

class Rob:
    
    type = None
        # 'random' - randomly places robber and robs randomly from enemy if able

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