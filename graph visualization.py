import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    G = nx.Graph()

    # Add vertices to the graph
    for vertex in graph.get_vertices():
        G.add_node(vertex)

    # Add edges to the graph
    for src, dest in graph.get_edges():
        G.add_edge(src, dest)

    # Position nodes using spring layout
    pos = nx.spring_layout(G, seed=42)

    # Draw the graph with labels and edge weights (if any)
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_weight='bold')

    # Add edge labels if the graph is weighted
    edge_labels = {(src, dest): f"{src}-{dest}" for src, dest in graph.get_edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Show the graph
    plt.title("Graph Visualization")
    plt.show()

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")

    visualize_graph(graph)
