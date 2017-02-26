from Board import Board
from Gameplay import Gameplay

class Catan:
    board = None
    gameplay = None

    def __init__( self ):
        self.board = Board()
        self.gameplay = Gameplay( self.board, 4 )
