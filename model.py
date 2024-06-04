import networkx as nx
import numpy as np

def generate_BA_model(G: nx.Graph, n: int, m: int, m0: int, seed: int = 0, nodes: tuple[int] = (2, 70)) -> tuple[nx.Graph, list, list]:
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

    # define 2 nodes that we will count the degree of
    node1 = nodes[0] + m0
    node2 = nodes[1] + m0
    degrees_node1 = []
    degrees_node2 = []
    
    # Add n - m0 nodes to the graph
    for i in range(m0, n):
        # Add m edges to the graph
        for _ in range(m):
            # Choose a random node to connect to
            node = np.random.choice(nodes_array)
            nodes_array = np.append(nodes_array, node) # Add the chosen node to the nodes array
            nodes_array = np.append(nodes_array, i) # Add the new node to the nodes array
            G.add_edge(i, node)
        
        # Calculate the degree of the two nodes
        if i >= node1:
            degrees_node1.append(G.degree[node1])
        if i >= node2:
            degrees_node2.append(G.degree[node2])
    
    return G, degrees_node1, degrees_node2

def generate_random_attachment_model(G: nx.Graph, n: int, m: int, m0: int, seed: int = 0, nodes: tuple[int] = (2, 70)) -> tuple[nx.Graph, list, list]:
    """
    Generates a model graph without the preferential attachment with n nodes and parameter m.
    """
    np.random.seed(seed)

    # Add m0 nodes to the graph
    G.add_nodes_from(range(m0))

    # Add edges between all nodes
    for i in range(m0):
        for j in range(i + 1, m0):
            G.add_edge(i, j)

    # define 2 nodes that we will count the degree of
    node1 = nodes[0] + m0
    node2 = nodes[1] + m0
    degrees_node1 = []
    degrees_node2 = []
    
    # Add n - m0 nodes to the graph
    for i in range(m0, n):
        # Add m edges to the graph
        for _ in range(m):
            # Choose a random node to connect to
            node = np.random.choice(range(i))
            G.add_edge(i, node)
        
        # Calculate the degree of the two nodes
        if i >= node1:
            degrees_node1.append(G.degree[node1])
        if i >= node2:
            degrees_node2.append(G.degree[node2])
    
    return G, degrees_node1, degrees_node2