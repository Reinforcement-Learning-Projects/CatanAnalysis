class Player:
    playerCode = "-"
    playerCodes = [ "@", "#", "$", "%" ]
    def __init__( self, id ):
        self.playerCode = self.playerCodes[id]