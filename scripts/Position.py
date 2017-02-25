# An intersection of three hexes
# hexes is a list of adjecent hexes and harbors
# adj links other adjecent positions together 
class Position:
    hexes = []
    harbor = " "
    adjPos = []
    owner = "^"
    playerId = None
    isCity = False
    def __init__( self, hexes ):
        self.hexes = hexes
    def setHarbor( self, harbor ):
        self.harbor = harbor
    def addAdjacentPosition( self, pos ):
        adjPos.append( pos )
    def asString( self ):
        string = self.harbor + self.owner
        if self.isCity:
            string += self.owner
        else:
            string += " "
        return string
