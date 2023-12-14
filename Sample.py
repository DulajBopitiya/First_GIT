import networkx as nx
import matplotlib.pyplot as plt

def calculate_edge_cost(conditions, selected_conditions):
    # Calculate edge cost based on selected conditions
    total_cost = 0
    for condition, weight in selected_conditions.items():
        if condition in conditions:
            total_cost += weight * conditions[condition]
    return total_cost

# Weighted graph representation
graph = {
    'Fort Hub': {'Bambalapitiya': {'distance': 0.55},
                 'Borella Junction': {'distance': 0.74},
                },
    'Bambalapitiya': {'Fort Hub': {'distance': 0.55},
                      'Kirulapana': {'distance': 0.52},
                      'Borella Junction': {'distance': 0.66},
                    },
    'Kirulapana': {'Bambalapitiya': {'distance': 0.52},
                   'Borella Junction': {'distance': 0.47},
                  },
    'Borella Junction': {'Fort Hub': {'distance': 0.74},
                         'Bambalapitiya': {'distance': 0.66},
                         'Kirulapana': {'distance': 0.47},
                        },
    'Malabe': {'Borella Junction': {'distance': 0.98},
               },
}

# Specify selected conditions for optimization
selected_conditions = {
    'distance': 1.0,  # Full weight for distance
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges with attributes
for source, destinations in graph.items():
    for destination, conditions in destinations.items():
        G.add_edge(source, destination, **conditions)

# Calculate and set edge weights based on selected conditions
for u, v, data in G.edges(data=True):
    edge_cost = calculate_edge_cost(data, selected_conditions)
    G[u][v]['weight'] = edge_cost

# Draw the graph
pos = nx.spring_layout(G)
edge_labels = {(u, v): f"{data['distance']}" for u, v, data in G.edges(data=True)}

nx.draw(G, pos, with_labels=True, node_size=900, node_color='skyblue', font_size=8, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.show()
