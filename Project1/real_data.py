import os
import numpy as np

# directory name storing graph data
DIR_NAME = 'graph-data'

# Function converts edge list into adjacency matrix
#
# data - edge list
def getAdjacencyFromCSV(data):
    vertexNo = np.max(data) + 1
    adjacencyMatrix = np.zeros((vertexNo, vertexNo), dtype=np.int64)
    
    for x in data:
        adjacencyMatrix[x[0]][x[1]] = 1

    return adjacencyMatrix
    

# Function reads CSV file
#
# filename - name of the csv to be read
def readDataFromCSV(filename):
    file_absolute_path = os.path.dirname(__file__)
    file_path = os.path.join(file_absolute_path, DIR_NAME, filename)

    with open(file_path) as file:
        lines = (line for line in file if not line.startswith("#"))
        data = np.loadtxt(lines, delimiter=',', skiprows=1, dtype=np.int64)
        return getAdjacencyFromCSV(data)


# data set information: Nodes: 50,515  Edges:  819,306
def importFacebookArtistData():
    return readDataFromCSV('artist_edges.csv')
    
# data set information: Nodes: 3,892  Edges:  17,262
def importFacebookTvShowData():
    return readDataFromCSV('tvshow_edges.csv')