from collections import deque

class GraphAlgorithms:
    def __init__(self, graph):
        self.graph = graph

    def dfs(self, start_vertex):
        visited = set()
        traversal_order = []

        def dfs_recursive(vertex):
            visited.add(vertex)
            traversal_order.append(vertex)
            for neighbor in self.graph.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start_vertex)
        return traversal_order

    def bfs(self, start_vertex):
        visited = set()
        traversal_order = []
        queue = deque([start_vertex])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                for neighbor in self.graph.get_neighbors(vertex):
                    if neighbor not in visited:
                        queue.append(neighbor)

        return traversal_order

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.graph.get_vertices()}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            dist_u, u = heapq.heappop(priority_queue)
            if dist_u > distances[u]:
                continue
            for v in self.graph.get_neighbors(u):
                dist_v = dist_u + 1  # For unweighted graph, set distance to 1
                if dist_v < distances[v]:
                    distances[v] = dist_v
                    heapq.heappush(priority_queue, (dist_v, v))

        return distances

    def prim_mst(self, start_vertex):
        mst = []
        visited = set()
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            weight, u = heapq.heappop(priority_queue)
            if u not in visited:
                visited.add(u)
                if u != start_vertex:  # Skip the first iteration where parent is None
                    mst.append((parent, u, weight))
                for v in self.graph.get_neighbors(u):
                    if v not in visited:
                        heapq.heappush(priority_queue, (weight + 1, v))
                        parent = u  # Track parent for MST edges

        return mst


# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")

    algorithms = GraphAlgorithms(graph)
    print("DFS Traversal:", algorithms.dfs("A"))
    print("BFS Traversal:", algorithms.bfs("A"))
    print("Shortest Distances from A:", algorithms.dijkstra("A"))
    print("Minimum Spanning Tree (Prim's Algorithm):", algorithms.prim_mst("A"))
