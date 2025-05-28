import osmnx as ox
import pickle

# Create a graph of a city (e.g., Chennai)
place = "Chennai, India"
G = ox.graph_from_place(place, network_type='drive')

# Confirm CRS is set
print("CRS:", G.graph['crs'])  # Should print 'epsg:4326' or similar

# Save the graph to a file using pickle
with open("data/road_graph.gpickle", "wb") as f:
    pickle.dump(G, f)
