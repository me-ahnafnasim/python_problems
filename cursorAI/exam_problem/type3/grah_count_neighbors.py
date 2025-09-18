"""
A graph is stored on an edge list implemented as a list of tuples. Each tuple contains two values,
 representing the nodes at the ends of an edge. Implement the Python function graphc(graph) that returns the nodes 
 (if any) having no less than 3 connections to other nodes of the graph.
"""

def graph7(graph):
    adjacency ={}
    for edge in graph:
        u,v = edge
        if u not in adjacency:
            adjacency[u] =[]
        if v not in adjacency:
            adjacency[v] =[]

        adjacency[u].append(v)
        adjacency[v].append(u)
    
    result =[]
    for node in adjacency:
        if len(adjacency[node]) >=3:
            result.append(node)

    return result
    
graph = [(1,4), (1,3), (2,3), (2,5)]  
print(graph7(graph))

















"""def adjacency_list_to_edge_list(graph):
    # Initialize an empty list to store edges
    edge_list = []

    # Iterate over each node in the graph
    for u in graph:
        # Get the neighbors of node u
        neighbors = graph[u]
        #print(u)
        # Iterate over each neighbor v
        for v in neighbors:
            #print("edge", v)
            # Ensure that the edge (u, v) is added only once (u < v)
            if u < v:
                edge_list.append((u, v))

    return edge_list

# Example usage
graph = {
    1: [2, 3, 4],
    2: [1, 3, 4],
    3: [2, 4, 1],
    4: [3, 1, 2]
}

edge_list = adjacency_list_to_edge_list(graph)
print("Edge List:", edge_list)"""









"""
def graph6(graph):
    # Step 1: Create an adjacency list
    adjacency = {}  # Dictionary-like structure

    for edge in graph:
        u, v = edge  # Extract nodes from the edge

        # if u in adjacency:
        #     pass
        # else:
        #     adjacency[u] = []

        # Manually handling dictionary behavior without built-in functions
        if u not in adjacency:
            adjacency[u] = []
        if v not in adjacency:
            adjacency[v] = []
        
        adjacency[u].append(v)
        adjacency[v].append(u)
    #Yes, this function converts an edge list to an adjacency list.
    print(adjacency)
    # Step 2: Collect nodes with exactly two neighbors
    result = []
    for node in adjacency:
        print(node)
        count = 0
        for _ in adjacency[node]:  # Count neighbors
            count += 1

        if count >=3:
            result.append(node)

    return result


# Example Usage
graph = [(1, 2), (2, 3), (3, 1), (1, 4), (2, 5)]
print(graph6(graph))  # Output: [1, 2] (since nodes 1 and 2 each have 3 connections)

graph = [(1,4), (1,3), (2,3), (2,5)]
print(graph6(graph))  # Output: Nodes with exactly two neighbors"""





"""




def graph6(graph):
#create a adjacency list from a edge list
    adjacency = {}  
    for edge in graph:
        u, v = edge
        if u not in adjacency:
            adjacency[u] = []
        if v not in adjacency:
            adjacency[v] = []
        
        adjacency[u].append(v)
        adjacency[v].append(u)
#find the neibours from the adjacency list
    result = []
    for node in adjacency:
        if len(adjacency[node]) >= 2:  # Simplified neighbor count
            result.append(node)
    return result  # Return the result

graph = [(1,4), (1,3), (2,3), (2,5)]
print(graph6(graph))  # Now it will print the result"""
    
