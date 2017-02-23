from random import randint

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
    numbers = [ 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12 ]
    hexes = []
    positions = []

    def __init__( self ):
        self.hexes = self.__makeHexes()
        self.positions = self.__makePositions( self.hexes )

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
                number = 7
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
        positions = []
        # I'm just going to make them manually (all 54 of them (let's call it loop unrolling for speed))
        # First init them all then link them all
        # row 1
        positions.append( [ hexes[0] ] ) #1
        positions.append( [ hexes[0] ] ) #2
        positions.append( [ hexes[0], hexes[1] ] ) #3
        positions.append( [ hexes[1] ] ) #4
        positions.append( [ hexes[1], hexes[2] ] ) #5
        positions.append( [ hexes[2] ] ) #6
        positions.append( [ hexes[2] ] ) #7
        # row 2
        positions.append( [ hexes[3] ] ) #1
        positions.append( [ hexes[0], hexes[3] ] ) #2
        positions.append( [ hexes[0], hexes[3], hexes[4] ] ) #3
        positions.append( [ hexes[0], hexes[1], hexes[4] ] ) #4
        positions.append( [ hexes[1], hexes[4], hexes[5] ] ) #5
        positions.append( [ hexes[1], hexes[2], hexes[5] ] ) #6
        positions.append( [ hexes[2], hexes[5], hexes[6] ] ) #7
        positions.append( [ hexes[2], hexes[6] ] ) #8
        positions.append( [ hexes[6] ] ) #9
        # row 3
        positions.append( [ hexes[7] ] ) #1
        positions.append( [ hexes[3], hexes[7] ] ) #2
        positions.append( [ hexes[3], hexes[7], hexes[8] ] ) #3
        positions.append( [ hexes[3], hexes[4], hexes[8] ] ) #4
        positions.append( [ hexes[4], hexes[8], hexes[9] ] ) #5
        positions.append( [ hexes[4], hexes[5], hexes[9] ] ) #6
        positions.append( [ hexes[5], hexes[9], hexes[10] ] ) #7
        positions.append( [ hexes[5], hexes[6], hexes[10] ] ) #8
        positions.append( [ hexes[6], hexes[10], hexes[11] ] ) #9
        positions.append( [ hexes[6], hexes[11] ] ) #10
        positions.append( [ hexes[11] ] ) #11
        # row 4
        positions.append( [ hexes[7] ] ) #1
        positions.append( [ hexes[7], hexes[12] ] ) #2
        positions.append( [ hexes[7], hexes[8], hexes[12] ] ) #3
        positions.append( [ hexes[8], hexes[12], hexes[13] ] ) #4
        positions.append( [ hexes[8], hexes[9], hexes[13] ] ) #5
        positions.append( [ hexes[9], hexes[13], hexes[14] ] ) #6
        positions.append( [ hexes[9], hexes[10], hexes[14] ] ) #7
        positions.append( [ hexes[10], hexes[14], hexes[15] ] ) #8
        positions.append( [ hexes[10], hexes[11], hexes[15] ] ) #9
        positions.append( [ hexes[11], hexes[15] ] ) #10
        positions.append( [ hexes[11] ] ) #11
        # row 5
        positions.append( [ hexes[12] ] ); #1
        positions.append( [ hexes[12], hexes[16] ] ) #2
        positions.append( [ hexes[12], hexes[13], hexes[16] ] ) #3
        positions.append( [ hexes[13], hexes[16], hexes[17] ] ) #4
        positions.append( [ hexes[13], hexes[14], hexes[17] ] ) #5
        positions.append( [ hexes[14], hexes[17], hexes[18] ] ) #6
        positions.append( [ hexes[14], hexes[15], hexes[18] ] ) #7
        positions.append( [ hexes[15], hexes[18] ] ) #8
        positions.append( [ hexes[15] ] ) #9
        # row 6
        positions.append( [ hexes[16] ] ) #1
        positions.append( [ hexes[16] ] ) #2
        positions.append( [ hexes[16], hexes[17] ] ) #3
        positions.append( [ hexes[17] ] ) #4
        positions.append( [ hexes[17], hexes[18] ] ) #5
        positions.append( [ hexes[18] ] ) #6
        positions.append( [ hexes[18] ] ) #7

        return positions

    # prints the current board to the console
    def drawIt( self ):
        # how many hexagon locations per row (rows top to bottom and locs left to right)
        boardStringR = [ 3,4,4,4,5,5,5,6,6,6,5,5,5,4,4,4,3]
        # how many spaces before first symbol in each row
        boardStringS = [12,8,11,8,4,7,4,0,3,0,4,7,4,8,11,8,12]
        hexI = 0;
        for s in xrange( 0, len(boardStringS) ):
            strHead = "" # the begining line portion
            strAfter = "" # the repeatable line portion
            strRow = ""
            symbol = "*"
            gap = 7
            # check if it's a row with a label
            if (s+1)%3 == 0:
                # then we print the number and resource
                gap = 5
                strHead = (" " * boardStringS[s]) + ("%02d%s" % ( self.hexes[hexI].number, self.hexes[hexI].resource[0] ))
                hexI += 1
                strRow += strHead
                for x in xrange( 0, boardStringR[s]-2):
                    strRow += (" " * gap) + ("%02d%s" % ( self.hexes[hexI].number, self.hexes[hexI].resource[0] ))
                    hexI += 1
            else:
                strHead = (" " * boardStringS[s]) + symbol
                # 7 because it looked like a good width
                strAfter = (" " * gap) + symbol
                # -1 because we already put the head
                strRow = strHead + (strAfter * (boardStringR[s]-1))
            
            print( strRow )