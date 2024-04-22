import networkx as nx
import numpy as np

def generate_model(G: nx.Graph, n: int, m: int, m0: int, seed: int = 0) -> nx.Graph:
    """
    Generates a Barabási-Albert model graph with n nodes, m0 starting nodes and parameter m.
    """
    np.random.seed(seed)

    # Add m0 nodes to the graph
    G.add_nodes_from(range(m0))

    # Add edges between all nodes
    for i in range(m0):
        for j in range(i + 1, m0):
            G.add_edge(i, j)

    nodes_array = np.array(list(range(m0))*(m0-1)) # Create initial nodes array
    
    # Add n - m0 nodes to the graph
    for i in range(m0, n):
        # Add m edges to the graph
        for _ in range(m):
            # Choose a random node to connect to
            node = np.random.choice(nodes_array)
            nodes_array = np.append(nodes_array, node) # Add the chosen node to the nodes array
            nodes_array = np.append(nodes_array, i) # Add the new node to the nodes array
            G.add_edge(i, node)
    
    return G
