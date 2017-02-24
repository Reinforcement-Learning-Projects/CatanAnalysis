from random import randint
from random import shuffle

from Hex import Hex
from Position import Position

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
    shuffle( resources )
    numbers = [ 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12 ]
    shuffle( numbers )

    hexes = []
    positions = []

    def __init__( self ):
        self.hexes = self.__makeHexes()
        self.positions = self.__makePositions( self.hexes )
        self.__addHarbors()

    # The order of the hexes list signifies the placement of the hexes too:
    # With a flat side facing you: 0 = top left and 18 bottom right (much like reading)
    # such that the numbers of tiles in each row in order is: 3, 4, 5, 4, 3
    def __makeHexes( self ):
        hexes = [];
        # for each tile spot
        for h in xrange( 0, len( self.resources ) ):
            resource = self.resources.pop()

            if resource == 'desert':
                number = 7
            else:
                number = self.numbers.pop()

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
        positions = []
        # I'm just going to make them manually (all 54 of them (let's call it loop unrolling for speed))
        # First init them all then link them all
        # row 1
        positions.append( Position([ hexes[0] ]) ) #1
        positions.append( Position([ hexes[0] ]) ) #2
        positions.append( Position([ hexes[0], hexes[1] ]) ) #3
        positions.append( Position([ hexes[1] ]) ) #4
        positions.append( Position([ hexes[1], hexes[2] ]) ) #5
        positions.append( Position([ hexes[2] ]) ) #6
        positions.append( Position([ hexes[2] ]) ) #7
        # row 2
        positions.append( Position([ hexes[3] ]) ) #1
        positions.append( Position([ hexes[0], hexes[3] ]) ) #2
        positions.append( Position([ hexes[0], hexes[3], hexes[4] ]) ) #3
        positions.append( Position([ hexes[0], hexes[1], hexes[4] ]) ) #4
        positions.append( Position([ hexes[1], hexes[4], hexes[5] ]) ) #5
        positions.append( Position([ hexes[1], hexes[2], hexes[5] ]) ) #6
        positions.append( Position([ hexes[2], hexes[5], hexes[6] ]) ) #7
        positions.append( Position([ hexes[2], hexes[6] ]) ) #8
        positions.append( Position([ hexes[6] ]) ) #9
        # row 3
        positions.append( Position([ hexes[7] ]) ) #1
        positions.append( Position([ hexes[3], hexes[7] ]) ) #2
        positions.append( Position([ hexes[3], hexes[7], hexes[8] ]) ) #3
        positions.append( Position([ hexes[3], hexes[4], hexes[8] ]) ) #4
        positions.append( Position([ hexes[4], hexes[8], hexes[9] ]) ) #5
        positions.append( Position([ hexes[4], hexes[5], hexes[9] ]) ) #6
        positions.append( Position([ hexes[5], hexes[9], hexes[10] ]) ) #7
        positions.append( Position([ hexes[5], hexes[6], hexes[10] ]) ) #8
        positions.append( Position([ hexes[6], hexes[10], hexes[11] ]) ) #9
        positions.append( Position([ hexes[6], hexes[11] ]) ) #10
        positions.append( Position([ hexes[11] ]) ) #11
        # row 4
        positions.append( Position([ hexes[7] ]) ) #1
        positions.append( Position([ hexes[7], hexes[12] ]) ) #2
        positions.append( Position([ hexes[7], hexes[8], hexes[12] ]) ) #3
        positions.append( Position([ hexes[8], hexes[12], hexes[13] ]) ) #4
        positions.append( Position([ hexes[8], hexes[9], hexes[13] ]) ) #5
        positions.append( Position([ hexes[9], hexes[13], hexes[14] ]) ) #6
        positions.append( Position([ hexes[9], hexes[10], hexes[14] ]) ) #7
        positions.append( Position([ hexes[10], hexes[14], hexes[15] ]) ) #8
        positions.append( Position([ hexes[10], hexes[11], hexes[15] ]) ) #9
        positions.append( Position([ hexes[11], hexes[15] ]) ) #10
        positions.append( Position([ hexes[11] ]) ) #11
        # row 5
        positions.append( Position([ hexes[12] ]) ); #1
        positions.append( Position([ hexes[12], hexes[16] ]) ) #2
        positions.append( Position([ hexes[12], hexes[13], hexes[16] ]) ) #3
        positions.append( Position([ hexes[13], hexes[16], hexes[17] ]) ) #4
        positions.append( Position([ hexes[13], hexes[14], hexes[17] ]) ) #5
        positions.append( Position([ hexes[14], hexes[17], hexes[18] ]) ) #6
        positions.append( Position([ hexes[14], hexes[15], hexes[18] ]) ) #7
        positions.append( Position([ hexes[15], hexes[18] ]) ) #8
        positions.append( Position([ hexes[15] ]) ) #9
        # row 6
        positions.append( Position([ hexes[16] ]) ) #1
        positions.append( Position([ hexes[16] ]) ) #2
        positions.append( Position([ hexes[16], hexes[17] ]) ) #3
        positions.append( Position([ hexes[17] ]) ) #4
        positions.append( Position([ hexes[17], hexes[18] ]) ) #5
        positions.append( Position([ hexes[18] ]) ) #6
        positions.append( Position([ hexes[18] ]) ) #7

        return positions

    # adds harbors based on the 6 default ocean pieces
    def __addHarbors( self ):
        # 3 is 3:1 and the resource harbors match theit first letter
        harborPieces = [ ["3","s"],["3"],["3","b"],["w"],["3","g"],["o"] ]
        # randomize them
        shuffle( harborPieces )
        
        # list of pos index of where harbor should be placed (clockwise order from top)
        # index 0 for 1 harbor pieces and 1 for two harbor pieces
        possiblePos = [
            [
                [[2,3]],
                [[14,15]],
                [[36,46]],
                [[50,51]],
                [[38,39]],
                [[7,17]]
            ],
            [
                [[0,1],[3,4]],
                [[5,6],[15,25]],
                [[26,37],[45,46]],
                [[52,53],[49,50]],
                [[47,48],[28,38]],
                [[16,27],[7,8]]
            ]
        ]
        # set harbors: for each harbor in each harbor piece,
        # set both position that that harbor occupies based on
        # the number of the harbor piece and how many harbors are on that pieace
        for p in xrange( 0, len(harborPieces) ):
            piece = harborPieces[p]
            for h in xrange( 0, len(piece) ):
                for i in possiblePos[len(piece) - 1][p][h]:
                    self.positions[i].setHarbor( piece[h] ) 

    # prints the current board to the console
    def drawIt( self ):
        # I'm just going to contrust it line by line as it gets unessecarily complicated using loops
        h = []
        p = []
        for hex in self.hexes:
            h.append( hex.asString() )
        for pos in self.positions:
            p.append( pos.asString() )
        # Note: intermediate whitespace is ignored in strong modulo operation
        # and is their the maintain the same lengths
        print( "" ) 
        print( "                  % s         % s         % s                  " % (p[1],p[3],p[5]) )
        print( "            % s         % s         % s         % s            " % (p[0],p[2],p[4],p[6]) )
        print( "                                                               " )
        print( "                  % s         % s         % s                  " % (h[0],h[1],h[2]) )
        print( "                                                               " )
        print( "            % s         % s         % s         % s            " % (p[8],p[10],p[12],p[14]) )
        print( "      % s         % s         % s         % s         % s      " % (p[7],p[9],p[11],p[13],p[15]) )
        print( "                                                               " )
        print( "            % s         % s         % s         % s            " % (h[3],h[4],h[5],h[6]) )
        print( "                                                               " )
        print( "      % s         % s         % s         % s         % s      " % (p[17],p[19],p[21],p[23],p[25]) )
        print( "% s         % s         % s         % s         % s         % s" % (p[16],p[18],p[20],p[22],p[24],p[26]) )
        print( "                                                               " )
        print( "      % s         % s         % s         % s         % s      " % (h[7],h[8],h[9],h[10],h[11]) )
        print( "                                                               " )
        print( "% s         % s         % s         % s         % s         % s" % (p[27],p[29],p[31],p[33],p[35],p[37]) )
        print( "      % s         % s         % s         % s         % s      " % (p[28],p[30],p[32],p[34],p[36]) )
        print( "                                                               " )
        print( "            % s         % s         % s         % s            " % (h[12],h[13],h[14],h[15]) )
        print( "                                                               " )
        print( "      % s         % s         % s         % s         % s      " % (p[38],p[40],p[42],p[44],p[46]) )
        print( "            % s         % s         % s         % s            " % (p[39],p[41],p[43],p[45]) )
        print( "                                                               " )
        print( "                  % s         % s         % s                  " % (h[16],h[17],h[18]) )
        print( "                                                               " )
        print( "            % s         % s         % s         % s            " % (p[47],p[49],p[51],p[53]) )
        print( "                  % s         % s         % s                  " % (p[48],p[50],p[52]) )
        print( "" )