class Discard:
    
    type = None
        # 'random' - randomly discard floor(half) cards when over 8 cards when 7 rolls

    def __init__( self, type ):
        self.type = type

    def go( self ):
        if self.type == 'random':
            self.random()
    
    def random( self ):
        print( '    random' )