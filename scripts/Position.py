# An intersection of three hexes
# hexes is a list of adjecent hexes and harbors
# adj links other adjecent positions together 
from settings import printv

class Position:
    hexes = None
    harbor = None
    adjPos = None
    playerId = None
    isCity = None

    def __init__( self, hexes ):
        self.hexes = hexes
        self.adjPos = []
        self.harbor = " "
        self.playerId = None
        self.isCity = False

    def setHarbor( self, harbor ):
        self.harbor = harbor
    def setAdjPos( self, pos ):
        self.adjPos = pos
    def placeBuilding( self, playerId, isCity ):
        self.playerId = playerId
        self.isCity = isCity

    def asString( self ):

        if self.playerId is None:
            owner = "^"
        else:
            owner = str(self.playerId)

        string = self.harbor + owner

        if self.isCity:
            string += owner
        else:
            string += " "

        return string
