# I. Selection Sort

import heapq

a = [int(input(f"Enter value {i+1}: ")) for i in range(int(input("Total number of elements: ")))]
print("Unsorted Array:", a)

for i in range(len(a)):
    min_idx = i
    for j in range(i+1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]

print("Selection Sort")
print("Sorted Array:", a)

# DIJISKSTRAS ALGO
# import heapq
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    pq = [(0, start)]

    while pq:
        dist, current = heapq.heappop(pq)

        for neighbor, cost in graph[current].items():
            new_dist = dist + cost

            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distance

print(dijkstra(graph, 'A'))

# JOB SCHEDULING 

jobs = [
    ('J1', 2, 100),
    ('J2', 1, 50),
    ('J3', 2, 10),
    ('J4', 1, 20)
]

jobs.sort(key=lambda x: x[2], reverse=True)

result = []
time_slots = [False] * 3

for job in jobs:
    name, deadline, profit = job

    for j in range(deadline-1, -1, -1):
        if not time_slots[j]:
            time_slots[j] = True
            result.append(job)
            break

print("Selected Jobs:")
for job in result:
    print(job)

# PRISM MST 
# import heapq

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

def prim(graph, start):
    visited = set([start])
    edges = []

    for to, cost in graph[start].items():
        heapq.heappush(edges, (cost, start, to))

    mst = []

    while edges:
        cost, frm, to = heapq.heappop(edges)

        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))

            for next_node, next_cost in graph[to].items():
                if next_node not in visited:
                    heapq.heappush(edges, (next_cost, to, next_node))

    return mst

print(prim(graph, 'A'))

# KRUSHKALS ALGORITHM

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

def kruskal(graph):
    edges = []

    for u in graph:
        for v in graph[u]:
            edges.append((graph[u][v], u, v))

    edges.sort()

    parent = {}

    for node in graph:
        parent[node] = node

    def find(node):
        while parent[node] != node:
            node = parent[node]
        return node

    mst = []

    for cost, u, v in edges:
        root_u = find(u)
        root_v = find(v)

        if root_u != root_v:
            mst.append((u, v, cost))
            parent[root_u] = root_v

    return mst

print(kruskal(graph))

