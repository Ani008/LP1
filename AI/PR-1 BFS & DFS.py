# Implement depth first search algorithm and Breadth First Search 
# algorithm, Use an undirected graph and develop a recursive algorithm 
# for searching all the vertices of a graph or tree data structure.

# Graph (common for both DFS and BFS)
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F', 'G']),
    'D': set(['B']),
    'E': set(['B']),
    'F': set(['C']),
    'G': set(['C'])
}

# Depth First Search (DFS) - Recursive
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in sorted(graph[node]):
            dfs(graph, neighbor, visited)

# Breadth First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = [start]
    
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in sorted(graph[vertex]):
                if neighbor not in visited:
                    queue.append(neighbor)
                    
# Running DFS
print("DFS Traversal starting from B:")
dfs(graph, 'B', set())

print("\n")

# Running BFS
print("BFS Traversal starting from A:")
bfs(graph, 'A')
