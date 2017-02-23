# A Catan hex tile
# number is 7 when resouce is 'desert'
class Hex:
    resource = None
    number = None
    def __init__( self, resource, number ):
        self.resource = resource
        self.number = number