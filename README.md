# GmE 221 - Laboratory Exercise 2

## Overview
This laboratory performs a parcel-landuse overlay analysis using Python (Geopanads).
Spatial data are retrieved from PostGIS using minimal SQL.
Overlay, area computation, percentage calculation, and classification are executed in Python.
The final output is exported as GeoJSON file for visualization in QGIS.

---

## Environment Setup
- Python 3.14
- PostgreSQl with PostGIS
- GeoPandas, SQLAlchemy, psycopg2

---

## How to Run
1. Activate the virtual environment
2. Run `analysis.py` to execute the overlay and classification
3. Load the generated GeoJSON file in QGIS

---

## Outputs
- GeoJSON file: `output/dominant_residential.geojson`
- Visualization in QGIS

---

## Reflection
### Input Stage
In this step, I saw the difference between how geometry is stored in PostGIS versus how it is represented in GeoPandas. PostGIS keeps the geometry in a database-friendly storage format, while GeoPandas converts it into geometry objects that Python can actually manipulate. Since I’m only loading and converting data at this stage, it is purely an Input/Output operation and not yet analysis, nothing is being computed or interpreted. This follows the “Input - Process - Output” structure from Lecture 3, where Part B is clearly the Input phase that prepares the data before any spatial algorithms or processing happen.