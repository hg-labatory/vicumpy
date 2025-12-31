import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("streetnet.gpkg")
print(gdf.head())
print(len(gdf))

ax = gdf.plot(figsize=(8, 8), alpha=0.7)
plt.show()
