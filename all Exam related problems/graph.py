
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

    # Step 2: Collect nodes with exactly two neighbors
    result = []
    for node in adjacency:
        print(node)
        count = 0
        for _ in adjacency[node]:  # Count neighbors
            count += 1

        if count == 2:
            result.append(node)

    return result

# Example Usage
graph = [(1,4), (1,3), (2,3), (2,5)]
print(graph6(graph))  # Output: Nodes with exactly two neighbors








