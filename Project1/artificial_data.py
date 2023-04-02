import sys, os
import numpy as np
import clustbench

# Funcion impots data based on given parameters
#
# catalog - name of the catalog
# set - name of the set
# returns: ndarrays: data, labels
def importData(catalog, set):
    sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])

    clustbenchResult = clustbench.load_dataset(catalog, set, "clustering-data-v1")    
    return clustbenchResult[3], clustbenchResult[4] 

# Funtion returns the largest artificial data set
def importLargeArtificialData():
    # 2 dimensions, 1500 points
    return importData("sipu", "birch1")

# Funtion returns the medium artificial data set
def importBiggerArtificialData():
    # 3 dimensions, 1500 points
    return importData("wut", "mk4")
    
# Funtion returns the smallest artificial data set
def importSmallerArtificialData():
    # 2 dimensions, 192 points
    return importData("wut", "z1")