#!.venv\Scripts\python.exe

import json 
import geopandas as gpd
from shapely.geometry import LineString
import overpy
from config import country_code, admin_level_country, city_name, nameconvention, street_types_list, admin_level_city
import tqdm
import time
import pandas as pd

# with open("src/geodaten/city_daten.json", "r", encoding="utf-8") as f:
# city = json.load(f)

# with open("src/geodaten/relation_tags.json", "r", encoding="utf-8") as f:
# streets = json.load(f)


# bbox = city["boundingbox"]
list_of_gdf = []
list_of_queries = []


def build_area_query(country_code, admin_level_country, city_name, nameconvention):
    """Erzeugt eine Overpass-Query für Straßen eines bestimmten Typs innerhalb einer Stadt.

    Die Query filtert zuerst Land und Stadt als Areas und sucht dann nur innerhalb
    dieser Areas nach `way[highway=streettype]`, inklusive aller referenzierten Nodes.

    Args:
        country_code: ISO3166-1 Ländercode (z.B. DE).
        admin_level_country: Admin-Level des Landes (z.B. 2).
        city: Name der Stadt.
        nameconvention: OSM-Namensschlüssel (z.B. "name" oder "name:en").
        streettype: Highway-Typ (z.B. "primary", "residential").

    Returns:
        str: Overpass-QL Query-String.
    """

    for streettype in street_types_list:

        query = f"""
            area["ISO3166-1"={country_code}][admin_level={admin_level_country}]->.country;
            area["{nameconvention}"="{city_name}"][admin_level={admin_level_city}]->.city;
            way[highway={streettype}];
            (._;>;);
            out body;
            """

        list_of_queries.append(query)
    return list_of_queries


def parse_osm_result(result):
    data = {"id": [], "highway": [], "name": [], "geometry": []}

    for way in result.ways:
        print(way)
        # if "highway" in way.tags and way.tags["highway"] == "primary":
        line = LineString([(p.lon, p.lat) for p in way.nodes])

        data["id"].append(way.id)
        data["highway"].append(way.tags.get("highway"))
        data["name"].append(way.tags.get("name"))
        data["geometry"].append(line)
    # Capture all tags for each way as a dictionary

    # create a GeoDataFrame from the dictionary
    return gpd.GeoDataFrame(data, crs="EPSG:4326").to_crs("EPSG:31468")


def safe_query(api, query):

    try:
        return api.query(query)
    except overpy.exception.OverpassTooManyRequests:
        time.sleep(20)


if __name__ == "__main__":
    api = overpy.Overpass()

    list_of_queries = build_area_query(country_code, admin_level_country, city_name, nameconvention)

    for query in list_of_queries:
        print(query)
        result = safe_query(api, query)
        # if result is None:
        #     continue
        gdf = parse_osm_result(result)
        list_of_gdf.append(gdf)
        osm_streets_gdf = pd.concat(list_of_gdf, ignore_index=True)
        gdf.to_file("streetnet.gpkg", driver="GPKG")
