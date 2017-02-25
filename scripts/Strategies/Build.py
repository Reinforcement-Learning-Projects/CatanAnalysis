class Build:
    
    type = None
        # 'best' - builds something that leaves the players total points highest

    def __init__( self, type ):
        self.type = type

    def go( self ):
        if self.type == 'best':
            self.best()
    
    def best( self ):
        print( '    best' )
