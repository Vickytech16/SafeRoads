import networkx as nx
import geopandas as gpd
from shapely.geometry import Point, LineString
import pickle

with open("data/road_graph.gpickle", "rb") as f:
    G = pickle.load(f)

# Load safety grid polygons
grid_gdf = gpd.read_file("data/grid_polygons.geojson")
grid_gdf = grid_gdf.set_geometry("geometry")
grid_gdf = grid_gdf.to_crs(epsg=4326)

# Build spatial index for fast lookup
grid_sindex = grid_gdf.sindex

def get_safety_score(point: Point) -> float:
    """Returns the normalized safety score of the grid cell containing the point."""
    possible_matches_index = list(grid_sindex.intersection(point.bounds))
    possible_matches = grid_gdf.iloc[possible_matches_index]
    for _, row in possible_matches.iterrows():
        if row.geometry.contains(point):
            return row['safety_score_norm']
    return 0.0  # Default score for areas outside the grid

def edge_risk_weight(u, v, data, alpha=0.7):
    """
    Weighted cost = alpha * length + (1 - alpha) * (length * (1 - safety_score))
    This balances safety and efficiency.
    """
    geom = data.get('geometry')
    length = data.get('length', 1.0)
    
    if not isinstance(geom, LineString):
        return length  # Fallback to basic length if no geometry
    
    midpoint = geom.interpolate(0.5, normalized=True)
    score = get_safety_score(midpoint)  # score between 0 (unsafe) and 1 (safe)
    
    # Combine safety and distance
    risk_penalty = length * (1 - score)
    return alpha * length + (1 - alpha) * risk_penalty


def get_route(start_lat, start_lng, end_lat, end_lng):
    from osmnx.distance import nearest_nodes

    start_node = nearest_nodes(G, X=start_lng, Y=start_lat)
    end_node = nearest_nodes(G, X=end_lng, Y=end_lat)

    path = nx.shortest_path(G, start_node, end_node, weight=lambda u, v, d: edge_risk_weight(u, v, d, alpha=0.7))

    coords = []
    for u, v in zip(path[:-1], path[1:]):
        edge = G.get_edge_data(u, v)[0]
        geom = edge.get("geometry")
        if geom:
            coords.extend(list(geom.coords))
        else:
            coords.append((G.nodes[u]['x'], G.nodes[u]['y']))
            coords.append((G.nodes[v]['x'], G.nodes[v]['y']))

    return coords
