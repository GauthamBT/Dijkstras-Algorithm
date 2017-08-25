import sys

#Class to represent the graph
class UnDirectedGraph:
    def __init__(self, v):
        self.noOfVerticies = v
        self.adjacencyListArray = [{}]
        self.adjacencyListArray.clear()
        self.shortestPathArray = []
        self.shortestPathArray.clear()
        self.visitedArray = []
        self.visitedArray.clear()
        self.graphQueue = []
        self.graphQueue.clear()
        
        for i in range(v):
            self.adjacencyListArray.append({})
        
        for j in range(v):
            self.shortestPathArray.append(sys.maxsize)
            
        for k in range(v):
            self.visitedArray.append(False)

#Function to add edges and their weight
def addEdge(graph, src, dest, weight):
    #Saving neighbors and weights in dicts
    graph.adjacencyListArray[src].__setitem__(dest,weight)
    graph.adjacencyListArray[dest].__setitem__(src,weight)

def dijstrasFunction(graph):
    #Peforming dijkstras on all nodes
    while graph.graphQueue != list():
        dijkstrasAlgorithm(graph, graph.graphQueue.pop())

def dijkstrasAlgorithm(graph, source):
    #if the source has been visited, return
    if graph.visitedArray[source] == True:
        return
    
    tempArray = [] #To temporarily store the adjacenet sums
    tempArray.clear()
    leastIndex = 0 #To store the least element's index
    minValue = sys.maxsize #Value used to store the minimum value
    
    #print ("Before the adjacencyListArray Loop")
    #graph.adjacencyListArray[source] = Gives the list of adjacent nodes for the source
    #graph.adjacencyListArray[source].keys() = These are the keys of the adjacent node dict
    #list(graph.adjacencyListArray[source].keys())[i] = Gives linear access to the keys of adjacent nodes dict
    for i in range(graph.adjacencyListArray[source].__len__()):
        #tempAdd = Is a temporary value to store the new distance calculated
        tempAdd = graph.shortestPathArray[source] + graph.adjacencyListArray[source][list(graph.adjacencyListArray[source].keys())[i]]
        tempArray.append(tempAdd)
        
        #Updating the shortest path array
        if graph.shortestPathArray[list(graph.adjacencyListArray[source].keys())[i]] > tempAdd:
            graph.shortestPathArray[list(graph.adjacencyListArray[source].keys())[i]] = tempAdd
        
        #To find the least distance node
        if minValue > tempArray[i] and graph.visitedArray[list(graph.adjacencyListArray[source].keys())[i]] == False:
            minValue = tempArray[i]
            leastIndex = i
    
    #Adding least weight neighbors to the queue
    #Checking if the least distance node is already visited or not and also checking if it is in the queue.
    if graph.visitedArray[list(graph.adjacencyListArray[source].keys())[leastIndex]] == False and list(graph.adjacencyListArray[source].keys())[leastIndex] not in graph.graphQueue:
        graph.graphQueue.insert(0,list(graph.adjacencyListArray[source].keys())[leastIndex])
            
    #Adding the remaining neighbors to the queue
    i = 0
    for i in range(graph.adjacencyListArray[source].__len__()):
        #Checking if the node has been visited already or if it is already in the queue
        if graph.visitedArray[list(graph.adjacencyListArray[source].keys())[i]] == False and i != leastIndex and list(graph.adjacencyListArray[source].keys())[i] not in graph.graphQueue:
            graph.graphQueue.insert(0,list(graph.adjacencyListArray[source].keys())[i])
    
    #Marking the node as visited
    graph.visitedArray[source] = True
    
    #print ("End of dijkstras algorithm", graph.graphStack)
    #print ()

#To print the graph representation
def printGraph(graph):
    for i in range(0,graph.noOfVerticies):
        print ("For",i,"=",graph.adjacencyListArray[i])

#To print the shortest path
def printShortestPath(graph):
    for i in range(graph.noOfVerticies):
        print ("Shortest distance for",i,"=",graph.shortestPathArray[i])
    

#MAIN PROGRAM

# #Provide the number of vertices
# numberOfVertices = 9 
# #Select source of the graph
# source = 0
# 
# #Creating a graph
# graph = UnDirectedGraph(numberOfVertices)
# 
# #Making the source as 0.
# graph.shortestPathArray[source] = 0
# #Initiating the stack with source node
# graph.graphQueue.insert(0,source)
# 
# #Defining the edges of the undirected graph
# addEdge(graph, 0, 1, 4)
# addEdge(graph, 0, 7, 8)
# addEdge(graph, 1, 7, 11)
# addEdge(graph, 1, 2, 8)
# addEdge(graph, 7, 8, 7)
# addEdge(graph, 7, 6, 1)
# addEdge(graph, 2, 3, 7)
# addEdge(graph, 2, 5, 4)
# addEdge(graph, 2, 8, 2)
# addEdge(graph, 6, 5, 2)
# addEdge(graph, 6, 8, 6)
# addEdge(graph, 3, 4, 9)
# addEdge(graph, 3, 5, 14)
# addEdge(graph, 5, 4, 10)
# 
# dijstrasFunction(graph)
#  
# printShortestPath(graph)

