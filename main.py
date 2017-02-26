#!/usr/bin/python

import sys
import argparse

sys.path.insert( 0, 'scripts' )
sys.path.insert( 0, 'scripts/Strategies' )

import settings

from Catan import Catan

verbose = False

def parseArgs( args ):
    parser = argparse.ArgumentParser( description = 'Runs automated games of The Settlers of Catan for analysis.' )
    parser.add_argument('--verbose', '-v', action="store_true", default=False, help='Prints out details.')
    args = parser.parse_args()

    settings.setVerbose( args.verbose )

    return args

def printv( p ):
    if verbose:
        print p

if __name__ == "__main__":
    parseArgs( sys.argv )

    app = Catan()