import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("src\streetnet.gpkg")
print(gdf.columns)
gdf.plot()
plt.show()
