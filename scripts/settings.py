verbose = False

def printv( p ):
    if verbose:
        print p

def setVerbose( v ):
    global verbose
    verbose = v