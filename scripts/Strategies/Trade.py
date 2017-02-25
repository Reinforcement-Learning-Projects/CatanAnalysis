class Trade:
    
    type = None
        # 'none' - never trades with anyone

    def __init__( self, type ):
        self.type = type

    def go( self ):
        if self.type == 'none':
            self.none()
    
    def none( self ):
        print( '    none' )