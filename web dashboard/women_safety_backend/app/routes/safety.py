from fastapi import APIRouter
from fastapi.responses import JSONResponse, FileResponse
from app.utils import load_geojson, load_csv_data

router = APIRouter()

@router.get("/grid")
def get_grid_data():
    """Return GeoJSON grid with safety scores (for maps)."""
    data = load_geojson("data/grid_polygons.geojson")
    return JSONResponse(content=data)

@router.get("/stats")
def get_summary_stats():
    """Return average safety level stats (optional)."""
    df = load_csv_data("data/safety_data.csv")
    avg_score = round(df["safety_score"].mean(), 3)
    return {"average_safety_score": avg_score}
