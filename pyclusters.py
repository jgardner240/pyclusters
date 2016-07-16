# -*- coding: utf-8 -*-
def searchNeighbors(row,col):
    retval = 1 # We get here and this is a bad pixel
    tif[row,col] = 1 # mark the pixel so it's not bad anymore

    # result = {True: x, False: y}[a > b]
    rowMin = {True: row - 1, False: 0}[row > 0]
    colMin = {True: col - 1, False: 0}[col > 0]
    rowMax = {True: row + 1, False: rows - 1}[row < rows - 1]
    colMax = {True: col + 1, False: cols - 1}[col < cols - 1]
    
    for y in range(rowMin, rowMax+1):
        for x in range(colMin, colMax+1):
            if tif[y,x] == 0:
                retval += searchNeighbors(y,x)
                
    return retval

if __name__ == '__main__':
    import sys
    from tifffile import imread
    
    args = sys.argv[1:]
    bpcount = 0
    clusterCount = 0
    cluster = []
    bcl = []
    
    for arg in args:
        print(arg)
        tif = imread(arg)
        print(tif.dtype)
        rows = tif.shape[0]
        cols = tif.shape[1]

        
    for row in range(rows):
        for col in range(cols):
            if tif[row,col] == 0:
                bpcount += searchNeighbors(row,col)
                #print('Cluster #{:d} count: {:d}'.format(clusterCount,bpcount))
                bcl.append( [clusterCount, bpcount] )
                bpcount = 0
                clusterCount +=1

    print(len(bcl))