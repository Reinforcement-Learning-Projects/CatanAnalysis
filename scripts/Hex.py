# A Catan hex tile
# number is 7 when resouce is 'desert'
from settings import printv

class Hex:
    resource = None
    number = None
    def __init__( self, resource, number ):
        self.resource = resource
        self.number = number
    
    # as form nnR (padded number and uppercase first resource letter)
    def asString( self ):
        if self.resource is 'desert':
            return ' D '
        return "%02d%s" % ( self.number, self.resource[0].upper() )