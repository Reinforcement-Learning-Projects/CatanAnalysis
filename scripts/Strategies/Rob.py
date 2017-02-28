from settings import printv

from random import randint

class Rob:
    
    type = None
        # 'random' - randomly places robber and robs randomly from enemy if able
        # 'mostWithoutMe' - places the robber on the last found spot with the most enemy buildings without mine on it

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
        randHexI = randint( 0, len(self.Board.hexes) - 1 )
        printv( '    Moving robber from hex ' + str(self.Board.robberHexI) + ' to ' + str(randHexI) )
        self.Board.moveRobberTo( randHexI )

    def mostWithoutMe( self ):
        for h in self.Board.hexes:
            for p in h.surroundPos:
                printv( 'h' )