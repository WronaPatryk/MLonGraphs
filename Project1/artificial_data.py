

def importBiggerArtificialData():
    # 3 dimensions, 1500 points
    
    import sys, os
    import numpy as np
    sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])
    import clustbench
    
    clustbenchResult = clustbench.load_dataset("wut", "mk4", "clustering-data-v1")
    
    return clustbenchResult[3], clustbenchResult[4] # ndarrays: data, labels
    
    
def importSmallerArtificialData():
    # 2 dimensions, 192 points
    
    import sys, os
    import numpy as np
    sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])
    import clustbench
    
    clustbenchResult = clustbench.load_dataset("wut", "z1", "clustering-data-v1")

    return clustbenchResult[3], clustbenchResult[4] # ndarrays: data, labels