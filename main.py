from model import generate_model
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create a Barabási-Albert model graph with 100 nodes and parameter m = 2
G = nx.Graph()
m=1
G = generate_model(G, n=100000, m=m, m0=4, seed=42)

# Draw the graph
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True)
# plt.show()

# Draw the degree distribution
# degree_sequence = [d for n, d in G.degree()]
# deg, cnt = np.unique(degree_sequence, return_counts=True)
# cnt = cnt / sum(cnt)

degree_freq = nx.degree_histogram(G)
degrees = range(len(degree_freq))
degree_freq = [x / sum(degree_freq) for x in degree_freq]

plt.scatter(degrees[m:], degree_freq[m:])
plt.title("Degree Distribution of Barabási-Albert Model")
plt.ylabel("P(k)")
plt.xlabel("k")
plt.xscale('log')
plt.yscale('log')
plt.show()