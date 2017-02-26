from settings import printv

from Setup import Setup
from Discard import Discard
from Rob import Rob
from Trade import Trade
from Build import Build

# Algorithms for each phase
class Strategy:
    Setup = None
        # 'random' - randomly places initial settlements and roads
    Discard = None
        # 'random' - randomly discard floor(half) cards when over 8 cards when 7 rolls
    Rob = None
        # 'random' - randomly places robber and robs randomly from enemy if able
    Trade = None
        # 'none' - never trades with anyone
    Build = None
        # 'best' - builds something that leaves the players total points highest

    def __init__( self, playerId, board, players, setup='random', discard='random', rob='random', trade='none', build='best' ):
        self.Setup = Setup( setup, playerId, board, players )
        self.Discard = Discard( discard, playerId, board, players )
        self.Rob = Rob( rob, playerId, board, players )
        self.Trade = Trade( trade, playerId, board, players )
        self.Build = Build( build, playerId, board, players )

    def play( self, do ):
        do = do.lower()

        if do == 'setup':
            self.Setup.go()
        elif do == 'discard':
            self.Discard.go()
        elif do == 'rob':
            self.Rob.go()
        elif do == 'trade':
            self.Trade.go()
        elif do == 'build':
            self.Build.go()