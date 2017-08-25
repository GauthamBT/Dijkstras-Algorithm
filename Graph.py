from UnDirectedGraphClass import *

#Provide the number of vertices
numberOfVertices = 9 
#Select source of the graph
source = 0

#Creating a graph
graph = UnDirectedGraph(numberOfVertices)

#Making the source as 0.
graph.shortestPathArray[source] = 0
#Initiating the stack with source node
graph.graphQueue.insert(0,source)

#Defining the edges of the undirected graph
addEdge(graph, 0, 1, 4)
addEdge(graph, 0, 7, 8)
addEdge(graph, 1, 7, 11)
addEdge(graph, 1, 2, 8)
addEdge(graph, 7, 8, 7)
addEdge(graph, 7, 6, 1)
addEdge(graph, 2, 3, 7)
addEdge(graph, 2, 5, 4)
addEdge(graph, 2, 8, 2)
addEdge(graph, 6, 5, 2)
addEdge(graph, 6, 8, 6)
addEdge(graph, 3, 4, 9)
addEdge(graph, 3, 5, 14)
addEdge(graph, 5, 4, 10)

dijstrasFunction(graph)
 
printShortestPath(graph)