from fastapi import FastAPI
from pyproj import Transformer

app = FastAPI()

@app.get("/api/")
def read_root():
    return {"message": "API is working!"}

@app.get("/api/WGS84toGhanaNationalGrid/")
def wgs84_to_ghana_national_grid(lat: float, lon: float):
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:2136", always_xy=True)
    x, y = transformer.transform(lon, lat)
    return {"easting": x, "northing": y}

@app.get("/api/WGS84toGhanaMeterGrid/")
def wgs84_to_ghana_meter_grid(lat: float, lon: float):
    # Confirm EPSG:25000 exists or replace with the correct EPSG code for Ghana Meter Grid
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:25000", always_xy=True)
    x, y = transformer.transform(lon, lat)
    return {"easting": x, "northing": y}

@app.get("/api/GhanaNationalGridtoWGS84/")
def ghana_national_grid_to_wgs84(easting: float, northing: float):
    transformer = Transformer.from_crs("EPSG:2136", "EPSG:4326", always_xy=True)
    lon, lat = transformer.transform(easting, northing)
    return {"latitude": lat, "longitude": lon}

@app.get("/api/GhanaMeterGridtoWGS84/")
def ghana_meter_grid_to_wgs84(easting: float, northing: float):
    transformer = Transformer.from_crs("EPSG:25000", "EPSG:4326", always_xy=True)
    lon, lat = transformer.transform(easting, northing)
    return {"latitude": lat, "longitude": lon}
