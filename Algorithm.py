import networkx as nx
import matplotlib.pyplot as plt

# Weighted graph representation
graph = {
    'Fort Hub': {'Bambalapitiya': {'distance': 0.55},
                 'Borella Junction': {'distance': 0.74},
                 },
    'Bambalapitiya': {'Fort Hub': {'distance': 0.55},
                      'Kirulapana': {'distance': 0.52},
                      'Borella Junction': {'distance': 0.66}},
    'Kirulapana': {'Bambalapitiya': {'distance': 0.52},
                   'Borella Junction': {'distance': 0.47}},
    'Borella Junction': {'Fort Hub': {'distance': 0.74},
                         'Bambalapitiya': {'distance': 0.66},
                         'Kirulapana': {'distance': 0.47},
                         'Malabe': {'distance': 0.98}},
    'Malabe': {'Borella Junction': {'distance': 0.98},
               },
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges with attributes
for source, destinations in graph.items():
    for destination, conditions in destinations.items():
        G.add_edge(source, destination, **conditions)

# Use Dijkstra's algorithm to find the shortest path
shortest_path = nx.shortest_path(G, source='Fort Hub', target='Malabe', weight='distance')
shortest_path_length = nx.shortest_path_length(G, source='Fort Hub', target='Malabe', weight='distance')

# Draw the graph
pos = nx.spring_layout(G)
edge_labels = {(u, v): f"{data['distance']}" for u, v, data in G.edges(data=True)}

nx.draw(G, pos, with_labels=True, node_size=900, node_color='skyblue', font_size=8, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Highlight the shortest path in green
edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='green', width=2)

# Highlight the shortest path text in the graph
for i in range(len(shortest_path) - 1):
    plt.text(pos[shortest_path[i]][0], pos[shortest_path[i]][1] + 0.05, 'Shortest Path', color='green', ha='center')

plt.show()

print(f"Shortest Path: {shortest_path}")
print(f"Shortest Path Length: {shortest_path_length}")
