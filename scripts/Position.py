# An intersection of three hexes
# hexes is a list of adjecent hexes and harbors
# adj links other adjecent positions together 
class Position:
    hexes = []
    adjPos = []
    def __init__( self, hexes ):
        self.hexes = hexes
    def addAdjacentPosition( self, pos ):
        adjPos.append( pos )