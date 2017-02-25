class Setup:
    
    type = None
        # 'random' - randomly places initial settlements and roads

    def __init__( self, type ):
        self.type = type

    def go( self ):
        if self.type == 'random':
            self.random()
    
    def random( self ):
        print( '    random' )