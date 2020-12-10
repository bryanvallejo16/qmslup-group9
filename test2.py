# Import necessary modules
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon

# Filepath
fp = r"C:/Users/Saku/Desktop/Temp_GIS/QMSLUP/library_accessibility/qmslup-group9/data/libraries.txt"

# Read the data
data = pd.read_csv(fp, sep=';')

# Import the geocoding tool
from geopandas.tools import geocode

# Geocode addresses using Nominatim. Remember to provide a custom
# "application name" in the user_agent parameter!
geo = geocode(data['addr'], provider='nominatim'
              , user_agent='qmslup_ss', timeout=4)

join = geo.join(data)
join.head()

# Output file path
# outfp = r"C:/Users/Saku/Desktop/Temp_GIS/QMSLUP/library_accessibility/qmslup-group9/data/addresses.shp"

# Save to Shapefile
# join.to_file(outfp)

import os

ykr = gpd.read_file("C:/Users/Saku/Desktop/Temp_GIS/QMSLUP/library_accessibility/MetropAccess_YKR_grid/MetropAccess_YKR_grid_EurefFIN.shp")
geo = join.to_crs("EPSG:3067")

selection = gpd.sjoin(ykr, geo, how="inner", op='contains')
            
# Output file path
# outfp = r"C:/Users/Saku/Desktop/Temp_GIS/QMSLUP/library_accessibility/qmslup-group9/data/squares.shp"

# Save to Shapefile
# selection.to_file(outfp)

join_ids = []
for ykr_id in selection['YKR_ID']:
    join_ids.append(ykr_id)

out_fp = r"C:\Users\Saku\Desktop\Temp_GIS\QMSLUP\library_accessibility\qmslup-group9\data"

import filefinder

files = filefinder.filefinder(r"C:\Users\Saku\Desktop\Temp_GIS\QMSLUP\library_accessibility\HelsinkiTravelTimeMatrix2018"
                      , out_fp
                      , join_ids)

import tablejoiner

for fp in files:
    tablejoiner.tablejoiner(fp
                , r"C:\Users\Saku\Desktop\Temp_GIS\QMSLUP\library_accessibility\MetropAccess_YKR_grid\MetropAccess_YKR_grid_EurefFIN.shp"
                , out_fp)