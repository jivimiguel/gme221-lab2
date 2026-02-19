import geopandas as gpd
from sqlalchemy import create_engine

# Database connection
host = "localhost"
port = "5432"
dbname = "gme221"
user = "postgres"
password = "jivimigols8118"

# Create connection string
conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

# Create SQLAlchemy engine
engine = create_engine(conn_str)

# Load data
parcels = gpd.read_postgis("SELECT parcel_pin, geom FROM public.parcel", engine, geom_col="geom")
landuse = gpd.read_postgis("SELECT name, geom FROM public.landuse", engine, geom_col="geom")

# Reproject for area calculations
parcels = parcels.to_crs(epsg=3395)
landuse = landuse.to_crs(epsg=3395)

# Compute parcel area
parcels["total_area"] = parcels.geometry.area

# Overlay
overlay = gpd.overlay(parcels, landuse, how="intersection")
overlay["landuse_area"] = overlay.geometry.area
overlay["percentage"] = (overlay["landuse_area"] / overlay["total_area"]) * 100
overlay["percentage"] = overlay["percentage"].round(2)

# Find max percentage by parcel
max_pct = overlay.groupby("parcel_pin")["percentage"].max().reset_index()

# Keep parcels where no single landuse exceeds 60%
mixed = max_pct[max_pct["percentage"] <= 60]

# Attach geometry back
geom = overlay[["parcel_pin", "geometry"]].dissolve(by="parcel_pin").reset_index()
result = geom.merge(mixed, on="parcel_pin")

# Reproject to EPSG:4326
result = result.to_crs(epsg=4326)

# Export to GeoJSON
result.to_file("output/challenge_result.geojson", driver="GeoJSON")
print("Challenge result saved.")