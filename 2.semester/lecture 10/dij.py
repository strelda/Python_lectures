def dijkstra(graph: dict, start: str, end: str) -> tuple:
    """Dijkstra's algorithm to find the shortest path in a graph."""
    dist = {node: float('infinity') for node in graph}
    dist[start] = 0

    last_visited = {node: None for node in graph}
    print(last_visited)

# Example graph
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 7},
    'C': {'D': 3, 'E': 5},
    'D': {'E': 2, 'F': 6},
    'E': {'F': 4},
    'F': {}
}

# Find the shortest path
dijkstra(graph, 'A', 'F')
# shortest_path, total_distance = dijkstra(graph, 'A', 'F')

# print(f"Shortest path: {' → '.join(shortest_path)}")
# print(f"Total distance: {total_distance}")