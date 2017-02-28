# A Catan hex tile
# number is 7 when resouce is 'desert'
from settings import printv

class Hex:
    surroundingPos = None
    resource = None
    number = None
    hasRobber = False

    def __init__( self, resource, number ):
        self.surroundingPos = []
        self.resource = resource
        self.number = number
        self.hasRobber = False
    
    def pushPos( self, pos ):
        self.surroundingPos.append( pos )

    def placeRobber( self ):
        self.hasRobber = True
    def removeRobber( self ):
        self.hasRobber = False

    # as form nnR (padded number and uppercase first resource letter)
    def asString( self ):
        if self.resource is 'desert':
            return ' D '
        if self.hasRobber is True:
            hexRes = 'X'
        else:
            hexRes = self.resource[0].upper()

        return "%02d%s" % ( self.number, hexRes )