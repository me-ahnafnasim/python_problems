def vertices(graph, node1):
 nodes = []
 for edge in graph:
        for node in edge:
            if node not in nodes:
                nodes.append(node)
 print(nodes)

graph = [(1, 2), (2, 3), (3, 4), (4, 1)]
node1 = 2 #no contribution on the code
result = vertices(graph, node1)
print("Vertices of the graph:", result)



