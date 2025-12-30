from pathlib import Path
import geopandas as gpd
import pandas as pd
from typing import Iterable


class GeopackageRepository:
    def __init__(self, filepath: str | Path):
        self.filepath = Path(filepath)

    def create_gdf(self, records) -> gpd.GeoDataFrame:
        return gpd.GeoDataFrame(
            records,
            crs="EPSG:4326"
        ).to_crs("EPSG:31468")

    @staticmethod
    def concat(gdfs: Iterable[gpd.GeoDataFrame]) -> gpd.GeoDataFrame:
        return pd.concat(gdfs, ignore_index=True) # type: ignore

    def save(self, gdf: gpd.GeoDataFrame) -> None:
        gdf.to_file(self.filepath, driver="GPKG")
