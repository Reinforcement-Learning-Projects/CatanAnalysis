from settings import printv

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
                'ore', 'ore', 'ore' ]
                # 'desert' ] desert is added specially later
    numbers = None
    hexes = None
    robberHexI = None
    positions = None

    def __init__( self ):
        shuffle( self.resources )
        self.numbers = self.__makeHexNumbers()

        self.hexes = self.__makeHexes()
        self.positions = self.__makePositions( self.hexes )
        self.__linkHexesBackToPositions()
        self.__addHarbors()
        self.__connectPositions()

    def moveRobberTo( self, hexI ):
        self.hexes[self.robberHexI].removeRobber()
        self.hexes[hexI].placeRobber()
        self.robberHexI = hexI

    # The order of the hexes list signifies the placement of the hexes too:
    # With a flat side (of the board) facing you: 0 = top left and 18 bottom right (much like reading)
    # such that the numbers of tiles in each row in order is: 3, 4, 5, 4, 3
    def __makeHexes( self ):
        hexes = [];
        # for each tile spot
        for h in xrange( 0, len( self.numbers ) ):
            number = self.numbers.pop()
            if number is 7:
                resource = 'desert'
                self.robberHexI = len( hexes )
            else:
                resource = self.resources.pop()  

            # and finally make the hex
            hex = Hex( resource, number )
            hexes.append( hex )

        return hexes

    # returns a valid number arrangement (no 6's or 8's touching other 6's or 8's) 
    def __makeHexNumbers( self ):
        numbers = [ 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 7, 8, 9, 9, 10, 10, 11, 11, 12 ]

        def test68( v ):
                return (numbers[v] is 6) or (numbers[v] is 8)
        def testNumbers():
            invalid = False
            if test68(0):
                invalid = test68(1) or test68(3) or test68(4) or invalid
            if test68(1):
                invalid = test68(0) or test68(2) or test68(4) or test68(5) or invalid
            if test68(2):
                invalid = test68(1) or test68(5) or test68(6) or invalid
            if test68(3):
                invalid = test68(0) or test68(4) or test68(7) or test68(8) or invalid
            if test68(4):
                invalid = test68(0) or test68(1) or test68(3) or test68(5) or test68(8) or test68(9) or invalid
            if test68(5):
                invalid = test68(1) or test68(2) or test68(4) or test68(6) or test68(9) or test68(10) or invalid
            if test68(6):
                invalid = test68(2) or test68(5) or test68(10) or test68(11) or invalid
            if test68(7):
                invalid = test68(3) or test68(8) or test68(12) or invalid
            if test68(8):
                invalid = test68(3) or test68(4) or test68(7) or test68(9) or test68(12) or test68(13) or invalid
            if test68(9):
                invalid = test68(4) or test68(5) or test68(8) or test68(10) or test68(13) or test68(14) or invalid
            if test68(10):
                invalid = test68(5) or test68(6) or test68(9) or test68(11) or test68(14) or test68(15) or invalid
            if test68(11):
                invalid = test68(6) or test68(10) or test68(15) or invalid
            if test68(12):
                invalid = test68(7) or test68(8) or test68(13) or test68(16) or invalid
            if test68(13):
                invalid = test68(8) or test68(9) or test68(12) or test68(14) or test68(16) or test68(17) or invalid
            if test68(14):
                invalid = test68(9) or test68(10) or test68(13) or test68(15) or test68(17) or test68(18) or invalid
            if test68(15):
                invalid = test68(10) or test68(11) or test68(14) or test68(18) or invalid
            if test68(16):
                invalid = test68(12) or test68(13) or test68(17) or invalid
            if test68(17):
                invalid = test68(13) or test68(14) or test68(16) or test68(18) or invalid
            if test68(18):
                invalid = test68(14) or test68(15) or test68(17) or invalid

            return invalid
        
        invalid = True
        while invalid:
            shuffle( numbers )
            invalid = testNumbers()

        return numbers
                
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

    def __linkHexesBackToPositions( self ):
        for pos in self.positions:
            for hex in pos.hexes:
                hex.pushPos( pos )

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
    
    # Now say which positions are connected to which
    def __connectPositions( self ):
        self.positions[0].setAdjPos( [ self.positions[2], self.positions[8] ] )
        self.positions[1].setAdjPos( [ self.positions[0], self.positions[2] ] )
        self.positions[2].setAdjPos( [ self.positions[1], self.positions[3], self.positions[9] ] )
        self.positions[3].setAdjPos( [ self.positions[2], self.positions[4] ] )
        self.positions[4].setAdjPos( [ self.positions[3], self.positions[5], self.positions[12] ] )
        self.positions[5].setAdjPos( [ self.positions[4], self.positions[6] ] )
        self.positions[6].setAdjPos( [ self.positions[5], self.positions[14] ] )
        self.positions[7].setAdjPos( [ self.positions[8], self.positions[17] ] )
        self.positions[8].setAdjPos( [ self.positions[0], self.positions[7], self.positions[9] ] )
        self.positions[9].setAdjPos( [ self.positions[8], self.positions[10], self.positions[19] ] )
        self.positions[10].setAdjPos([ self.positions[2], self.positions[9], self.positions[11] ] )
        self.positions[11].setAdjPos([ self.positions[10], self.positions[12], self.positions[21] ] )
        self.positions[12].setAdjPos([ self.positions[4], self.positions[11], self.positions[13] ] )
        self.positions[13].setAdjPos([ self.positions[12], self.positions[14], self.positions[23] ] )
        self.positions[14].setAdjPos([ self.positions[6], self.positions[13], self.positions[15] ] )
        self.positions[15].setAdjPos([ self.positions[14], self.positions[25] ] )
        self.positions[16].setAdjPos([ self.positions[17], self.positions[27] ] )
        self.positions[17].setAdjPos([ self.positions[7], self.positions[16], self.positions[18] ] )
        self.positions[18].setAdjPos([ self.positions[17], self.positions[19], self.positions[29] ] )
        self.positions[19].setAdjPos([ self.positions[9], self.positions[18], self.positions[20] ] )
        self.positions[20].setAdjPos([ self.positions[19], self.positions[21], self.positions[31] ] )
        self.positions[21].setAdjPos([ self.positions[11], self.positions[20], self.positions[22] ] )
        self.positions[22].setAdjPos([ self.positions[21], self.positions[23], self.positions[33] ] )
        self.positions[23].setAdjPos([ self.positions[13], self.positions[22], self.positions[24] ] )
        self.positions[24].setAdjPos([ self.positions[23], self.positions[25], self.positions[35] ] )
        self.positions[25].setAdjPos([ self.positions[15], self.positions[24], self.positions[26] ] )
        self.positions[26].setAdjPos([ self.positions[25], self.positions[37] ] )
        self.positions[27].setAdjPos([ self.positions[16], self.positions[28] ] )
        self.positions[28].setAdjPos([ self.positions[27], self.positions[29], self.positions[38] ] )
        self.positions[29].setAdjPos([ self.positions[18], self.positions[28], self.positions[30] ] )
        self.positions[30].setAdjPos([ self.positions[29], self.positions[31], self.positions[40] ] )
        self.positions[31].setAdjPos([ self.positions[20], self.positions[30], self.positions[32] ] )
        self.positions[32].setAdjPos([ self.positions[31], self.positions[33], self.positions[42] ] )
        self.positions[33].setAdjPos([ self.positions[22], self.positions[32], self.positions[34] ] )
        self.positions[34].setAdjPos([ self.positions[33], self.positions[35], self.positions[44] ] )
        self.positions[35].setAdjPos([ self.positions[24], self.positions[34], self.positions[36] ] )
        self.positions[36].setAdjPos([ self.positions[35], self.positions[37], self.positions[46] ] )
        self.positions[37].setAdjPos([ self.positions[26], self.positions[36] ] )
        self.positions[38].setAdjPos([ self.positions[28], self.positions[39] ] )
        self.positions[39].setAdjPos([ self.positions[38], self.positions[40], self.positions[47] ] )
        self.positions[40].setAdjPos([ self.positions[30], self.positions[39], self.positions[41] ] )
        self.positions[41].setAdjPos([ self.positions[40], self.positions[42], self.positions[49] ] )
        self.positions[42].setAdjPos([ self.positions[32], self.positions[41], self.positions[43] ] )
        self.positions[43].setAdjPos([ self.positions[42], self.positions[44], self.positions[51] ] )
        self.positions[44].setAdjPos([ self.positions[34], self.positions[43], self.positions[45] ] )
        self.positions[45].setAdjPos([ self.positions[44], self.positions[46], self.positions[53] ] )
        self.positions[46].setAdjPos([ self.positions[36], self.positions[45] ] )
        self.positions[47].setAdjPos([ self.positions[39], self.positions[48] ] )
        self.positions[48].setAdjPos([ self.positions[47], self.positions[49] ] )
        self.positions[49].setAdjPos([ self.positions[41], self.positions[48], self.positions[50] ] )
        self.positions[50].setAdjPos([ self.positions[49], self.positions[51] ] )
        self.positions[51].setAdjPos([ self.positions[43], self.positions[50], self.positions[52] ] )
        self.positions[52].setAdjPos([ self.positions[51], self.positions[53] ] )
        self.positions[53].setAdjPos([ self.positions[45], self.positions[52] ] )

        

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
        printv( "" ) 
        printv( "                  % s         % s         % s                  " % (p[1],p[3],p[5]) )
        printv( "            % s         % s         % s         % s            " % (p[0],p[2],p[4],p[6]) )
        printv( "                                                               " )
        printv( "                  % s         % s         % s                  " % (h[0],h[1],h[2]) )
        printv( "                                                               " )
        printv( "            % s         % s         % s         % s            " % (p[8],p[10],p[12],p[14]) )
        printv( "      % s         % s         % s         % s         % s      " % (p[7],p[9],p[11],p[13],p[15]) )
        printv( "                                                               " )
        printv( "            % s         % s         % s         % s            " % (h[3],h[4],h[5],h[6]) )
        printv( "                                                               " )
        printv( "      % s         % s         % s         % s         % s      " % (p[17],p[19],p[21],p[23],p[25]) )
        printv( "% s         % s         % s         % s         % s         % s" % (p[16],p[18],p[20],p[22],p[24],p[26]) )
        printv( "                                                               " )
        printv( "      % s         % s         % s         % s         % s      " % (h[7],h[8],h[9],h[10],h[11]) )
        printv( "                                                               " )
        printv( "% s         % s         % s         % s         % s         % s" % (p[27],p[29],p[31],p[33],p[35],p[37]) )
        printv( "      % s         % s         % s         % s         % s      " % (p[28],p[30],p[32],p[34],p[36]) )
        printv( "                                                               " )
        printv( "            % s         % s         % s         % s            " % (h[12],h[13],h[14],h[15]) )
        printv( "                                                               " )
        printv( "      % s         % s         % s         % s         % s      " % (p[38],p[40],p[42],p[44],p[46]) )
        printv( "            % s         % s         % s         % s            " % (p[39],p[41],p[43],p[45]) )
        printv( "                                                               " )
        printv( "                  % s         % s         % s                  " % (h[16],h[17],h[18]) )
        printv( "                                                               " )
        printv( "            % s         % s         % s         % s            " % (p[47],p[49],p[51],p[53]) )
        printv( "                  % s         % s         % s                  " % (p[48],p[50],p[52]) )
        printv( "" )