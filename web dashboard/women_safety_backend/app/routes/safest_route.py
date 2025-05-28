# app/routes/safest_route.py

from fastapi import APIRouter, Query
from app.core.graph_utils import get_route
from app.core.path_utils import refine_path  # Import the refine_path function

router = APIRouter()

@router.get("/safest-route")
def get_safest_route(
    start_lat: float = Query(...),
    start_lng: float = Query(...),
    end_lat: float = Query(...),
    end_lng: float = Query(...)
):
    # Get raw coordinates from the route calculation
    coords = get_route(start_lat, start_lng, end_lat, end_lng)
    
    # Refine the coordinates before returning them
    refined_coords = refine_path(coords)
    
    return refined_coords
