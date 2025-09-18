"""def graph6(graph):
    adjacency ={}
    for edge in  graph:
        u,v=edge
        if u not in adjacency:
            adjacency[u] = []
        if v not in adjacency:
            adjacency[v] = []
        
        adjacency[u].append(v)
        adjacency[v].append(u)

    result =[]
    for node in adjacency:
        print(len(adjacency[node]))
            
"""
"""
graph = [(1,4), (1,3), (2,3), (2,5)]  
print(graph6(graph))"""








