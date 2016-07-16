# -*- coding: utf-8 -*-
def searchNeighbors(row,col):
    tif[row,col] = 1 # mark the pixel so it's not bad anymore
    bpl.append( (row,col) ) # Add it to the bad pixel list
    currentCluster.append( (row,col) ) # And add it to the current cluster
    
    # Ternary operator:
    # result = {True: x, False: y}[a > b]
    rowMin = {True: row - 1, False: 0}[row > 0]
    colMin = {True: col - 1, False: 0}[col > 0]
    rowMax = {True: row + 1, False: rows - 1}[row < rows - 1]
    colMax = {True: col + 1, False: cols - 1}[col < cols - 1]
    
    for y in range(rowMin, rowMax+1):
        for x in range(colMin, colMax+1):
            if tif[y,x] == 0:
                searchNeighbors(y,x) # Recursion is sexy
                

if __name__ == '__main__':
    import sys
    from tifffile import imread
    args = sys.argv[1:]
    
    bcl = [] # List of clusters found
    bpl = [] # List of bad pixels found
    currentCluster = [] # Current cluster

    for arg in args:
        print(arg)
        tif = imread(arg)
        print(tif.dtype)
        rows = tif.shape[0]
        cols = tif.shape[1]

        
    for row in range(rows):
        for col in range(cols):
            if tif[row,col] == 0:
                searchNeighbors(row,col)
                bcl.append( (currentCluster) ) # Cluster is complete, add it to the list
                del(currentCluster)
                currentCluster = []


    # All code below has be shamelessly stolen from Stan Garrow     
    numClustersLenEq1 = sum(1 for c in bcl if len(c) == 1)
    numClustersLenGt1 = sum(1 for c in bcl if len(c)  > 1)
    maxClusterSize    = max(len(c) for c in bcl)

    hist = [0]*(maxClusterSize+1)
    for c in bcl:
        hist[len(c)] += 1

    print()    
    print( ' ************* SUMMARY ********************************************')
    print( ' * ')
    print( ' * Total Number of Bad Pixels: {:4d}'.format(len(bpl)))
    print( ' * ')
    print( ' *       Number of Singleton Clusters: {:4d} '.format( numClustersLenEq1 ))
    print( ' *   Number of Non-Singleton Clusters: {:4d} '.format( numClustersLenGt1 ))
    print( ' *           Total Number of Clusters: {:4d} '.format(len(bcl)))
    print( ' * ')
    print( ' *               Largest Cluster Size: {:4d} '.format( maxClusterSize ))
    print( ' * ')
    print( ' ******************************************************************')
    print( ' ************* HISTOGRAM ******************************************')

    for ii in range(1,len(hist)):
        if hist[ii] > 0:
            print( ' * {:4d} Clusters contain {:4d} Pixels. *'.format( hist[ii], ii ))

    print( ' ******************************************************************')

