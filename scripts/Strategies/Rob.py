class Rob:
    
    type = None
        # 'random' - randomly places robber and robs randomly from enemy if able

    def __init__( self, type ):
        self.type = type

    def go( self ):
        if self.type == 'random':
            self.random()
    
    def random( self ):
        print( '    random' )