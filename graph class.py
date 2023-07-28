class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, src, dest, directed=False):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.graph[src].append(dest)
        if not directed:
            self.graph[dest].append(src)

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for src, neighbors in self.graph.items():
            for dest in neighbors:
                edges.append((src, dest))
        return edges

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])

    def __str__(self):
        result = ""
        for src, neighbors in self.graph.items():
            result += f"{src}: {neighbors}\n"
        return result

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")

    print("Vertices:", graph.get_vertices())
    print("Edges:", graph.get_edges())
    print("Neighbors of A:", graph.get_neighbors("A"))

    print("Graph:")
    print(graph)
