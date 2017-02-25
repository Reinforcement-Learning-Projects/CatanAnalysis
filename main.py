#!/usr/bin/python

import sys
import argparse

sys.path.insert( 0, 'scripts' )
sys.path.insert( 0, 'scripts/Strategies' )

from Catan import Catan

def parseArgs( args ):
    parser = argparse.ArgumentParser( description = 'Runs automated games of The Settlers of Catan for analysis.' )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    app = Catan( parseArgs(sys.argv) )