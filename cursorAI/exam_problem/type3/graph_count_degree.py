
def degrees(graph):
    degree_dict = {}

    for edge in graph:
        u,v =edge

        if u in degree_dict:
            degree_dict[u] += 1
        else:
            degree_dict[u] = 1
        
        if v in degree_dict:
            degree_dict[v] += 1
        else:
            degree_dict[v] = 1
    
    return degree_dict

graph = [(1, 4), (1, 3), (2, 3), (2, 5)]
print(degrees(graph))  # Output: {1: 2, 4: 1, 3: 2, 2: 2, 5: 1}

