
"""
Extracted Text:

A graph is stored on an edge list implemented as a list of tuples. Each tuple contains two values, representing the nodes at the ends
 of an edge. Implement the Python function sameconnections(graph, node1, node2) 
 that returns **True** if the arguments node1 and node2 have exactly the same number of connections.
"""
def sameconnections(graph, node1, node2):
    adjacency = {}
    for edge in graph:
        u, v = edge
        if u not in adjacency:
            adjacency[u] = []
        if v not in adjacency:
            adjacency[v] = []
        
        adjacency[u].append(v)
        adjacency[v].append(u)
    
    # Check if both nodes exist in the graph
    if node1 not in adjacency or node2 not in adjacency:
        return False
    
    # Compare the number of connections
    return len(adjacency[node1]) == len(adjacency[node2])


graph = [(1,4), (1,3), (2,3), (2,5)]  
print(sameconnections(graph, 1, 5))







