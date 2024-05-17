from model import generate_model
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create a Barabási-Albert model graph with 100 nodes and parameter m = 2
G = nx.Graph()
m=3
m0=4
nodes = (2, 70)
n = 10000
G, degrees1, degrees2 = generate_model(G, n=n, m=m, m0=m0, seed=np.random.randint(100), nodes=nodes)

degree_freq = nx.degree_histogram(G)
degrees = range(len(degree_freq))
degree_freq = [x / sum(degree_freq) for x in degree_freq]

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].plot(degrees[m:], degree_freq[m:], 'o')
ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[0].set_xlabel('Degree')
ax[0].set_ylabel('Frequency')
ax[0].set_title('Degree distribution')

ax[1].plot(range(m0+nodes[0], n), degrees1, 'o', label=f'Node {nodes[0]}')
ax[1].plot(range(m0+nodes[1], n), degrees2, 'o', label=f'Node {nodes[1]}')
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xlabel('Number of nodes')
ax[1].set_ylabel('Degree')
ax[1].set_title('Degree of 2 chosen nodes')
ax[1].legend()

plt.tight_layout()
plt.show()
