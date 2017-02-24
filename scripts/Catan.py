from Board import Board
from Gameplay import Gameplay

class Catan:
    board = None
    gameplay = None

    def __init__( self, attributes ): 
        self.board = Board()
        self.board.drawIt()
        self.gameplay = Gameplay( self.board, 4 )
