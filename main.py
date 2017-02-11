#!/usr/bin/python

import sys
import argparse
from random import randint

def parseArgs( args ):
    parser = argparse.ArgumentParser( description = 'Runs automated games of The Settlers of Catan for analysis.' )
    args = parser.parse_args()
    return args

# A Catan hex tile
# number arbitrary when resouces = 'desert'
class Hex:
    resource = None
    number = None
    def __init__( self, resource, number ):
        self.resource = resource
        self.number = number

# An intersection of three hexes
# hexes is a list of adjecent hexes and harbors
# adj links other adjecent positions together 
class Position:
    def __init__( self, hexes, adj ):
        print( '2hi again' )

# Assembles a set of positions based on the default Catan board
# 4grain, 4sheep, 4wood, 3brick, 3ore, 1desert
# chits 2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12
class Board:
    resources = [ 'grain', 'grain', 'grain', 'grain',
                'sheep', 'sheep', 'sheep', 'sheep',
                'wood', 'wood', 'wood', 'wood',
                'brick', 'brick', 'brick',
                'ore', 'ore', 'ore',
                'desert' ]
    numbers = [ 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12 ]
    hexes = []
    positions = []

    def __init__( self ):
        self.hexes = self.__makeHexes()
        self.__makePositions( self.hexes )

    # The order of the hexes list signifies the placement of the hexes too:
    # With a flat side facing you: 0 = top left and 18 bottom right (much like reading)
    # such that the numbers of tiles in each row in order is: 3, 4, 5, 4, 3
    def __makeHexes( self ):
        hexes = [];
        # for each tile spot
        for h in xrange( 0, 19 ):
            # get a random resource from resources
            i = randint( 0, len(self.resources) - 1 )
            # store it
            resource = self.resources[i]
            # delete the original so we don't use it again
            del self.resources[i]

            if resource == 'desert':
                number = None
            else:
                # get a random number from numbers
                i = randint( 0, len(self.numbers) - 1 )
                # store it
                number = self.numbers[i]
                # delete the original so we don't use it again
                del self.numbers[i]

            # and finally make the hex
            hex = Hex( resource, number )
            hexes.append( hex )

        return hexes

    # Now imagine; actually let me make an ascii board... nevermind/maybe later.
    # Now imagine the setup described above makehexes. This time make mental horizontal cuts
    # though the center of the hexes of the board. You should have 5 cuts (1 for each row).
    # Between those cuts, the borders of the hexes make horizontal zig-zaggy lines.
    # The corners from left to right then top to bottom are the order of the positions.
    def __makePositions( self, hexes ):
        print( '' )

class CatanAnalysis:
    def __init__( self, attributes ): 
        board = Board()

if __name__ == "__main__":
    app = CatanAnalysis( parseArgs(sys.argv) )