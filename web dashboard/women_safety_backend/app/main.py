from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import geopandas as gpd

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/grid-data")
def get_grid_data():
    gdf = gpd.read_file("data/grid_polygons.geojson")
    return JSONResponse(content=gdf.__geo_interface__)
