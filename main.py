#!/usr/bin/python

import sys
import argparse

def parseArgs( args ):
    parser = argparse.ArgumentParser( description = 'Runs automated games of The Settlers of Catan for analysis.' )
    args = parser.parse_args()
    return args

class CatanAnalysis:
    def __init__( self, attributes ): 
        print( 'hi' )

if __name__ == "__main__":
    app = CatanAnalysis( parseArgs(sys.argv) )

# A Catan hex tile
# number arbitrary when resouces = 'desert'
class Hex:
    def __init__( self, resource, number ):
        print( 'hi again' )

# An intersection of three hexes
# hexes is a list of adjecent hexes and harbors
# adj links other adjecent positions together 
class Position:
    def __init__( self, hexes, adj ):
        print( 'hi again' )