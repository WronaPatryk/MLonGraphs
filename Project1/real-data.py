# directory name storing graph data
DIR_NAME = 'graph-data'


# helper function used to read CSV file
# filename - name of the csv to be read
def readDataFromCSV(filename):
    import os
    import numpy as np

    file_absolute_path = os.path.dirname(__file__)
    file_path = os.path.join(file_absolute_path, DIR_NAME, filename)

    with open(file_path) as file:
        lines = (line for line in file if not line.startswith("#"))
        return np.loadtxt(lines, delimiter=',', skiprows=1)


# data set information: Nodes: 50,515  Edges:  819,306
def importFacebookArtistData():
    return readDataFromCSV('artist_edges.csv')
    
# data set information: Nodes: 3,892  Edges:  17,262
def importFacebookTvShowData():
    return readDataFromCSV('tvshow_edges.csv')