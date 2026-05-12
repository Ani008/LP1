graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {'G': 2},
    'E': {'G': 2},
    'F': {'G': 1},
    'G': {}
}

heuristic = {
    'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 2, 'F': 1, 'G': 0
}

def a_star(start, goal):
    open_list = {start}
    g = {start: 0}
    parents = {start: None}

    while open_list:
        current = min(open_list, key=lambda x: g[x] + heuristic[x])  
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1] 

        open_list.remove(current)
        for neighbor, cost in graph[current].items():
            temp_g = g[current] + cost
            if neighbor not in g or temp_g < g[neighbor]:
                g[neighbor] = temp_g
                parents[neighbor] = current
                open_list.add(neighbor)

    return None
print("Path:", a_star('A', 'G'))
