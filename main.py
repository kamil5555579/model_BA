from model import generate_model
import networkx as nx
import matplotlib.pyplot as plt

# Create a Barabási-Albert model graph with 100 nodes and parameter m = 2
G = nx.Graph()
G = generate_model(G, 200000, 1, 4, 3)

# Draw the graph
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True)
# plt.show()