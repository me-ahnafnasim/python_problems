"""
student = {
    "name": "Alice",
    "age": 22,
    "course": "Data Science"
}


student = {
    1: [2, 3, 4],
    2: [1, 3, 4],
    3: [2, 4, 1],
    4: [3, 1, 2]
}

edge_list =[]

for u in student:
    neibhor = student[u]

    for v in neibhor:
        # print("v", v)
        # print("u", u)
        if u<v:
           edge_list.append((u,v))


print(edge_list)

NOTE: learn basic from above before jamping the real problem
"""






def adjacency_list_to_edge_list(graph):
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
print("Edge List:", edge_list)