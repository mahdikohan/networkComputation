import networkx as nx
import numpy as np
np.set_printoptions(precision=2)
# Step 1: Create a Barabási-Albert graph
n = 10  # Number of nodes
m = 2   # Number of edges per new node
G = nx.barabasi_albert_graph(n, m)

# Step 2: Assign initial weight of 1 to all edges
for u, v in G.edges():
    G[u][v]['weight'] = 1

# Step 3: Sort nodes by degree in descending order
nodes_sorted_by_degree = sorted(G.nodes(), key=lambda node: G.degree(node), reverse=True)

# Step 4: Normalize weights for each node in sorted order
normalized_nodes = set()
for node in nodes_sorted_by_degree:
    # Get all edges connected to the node
    neighbors = G[node]
    total_weight = sum(G[node][neighbor]['weight'] for neighbor in neighbors)
    
    # Normalize weights for edges connected to this node
    for neighbor in neighbors:
        normalized_weight = G[node][neighbor]['weight'] / total_weight
        # Update the weight to the minimum of the existing weight and the normalized weight
        if neighbor in normalized_nodes:
            G[node][neighbor]['weight'] = min(G[node][neighbor]['weight'], normalized_weight)
        else:
            G[node][neighbor]['weight'] = normalized_weight

    # Mark this node as normalized
    normalized_nodes.add(node)

# Step 5: Get the weighted adjacency matrix
adj_matrix = nx.to_numpy_array(G, weight='weight')

# Display the adjacency matrix
print("Weighted Adjacency Matrix:")
print(adj_matrix)
print(np.sum(adj_matrix, axis=1))
# # Display edges with their weights for verification
# print("\nEdges with final weights:")
# for u, v, weight in G.edges(data='weight'):
#     print(f"Edge {u}-{v}: Weight {weight:.4f}")
