#!.venv\Scripts\python.exe

import json 
import geopandas as gpd
from shapely.geometry import LineString   
from config import street_types_list
import overpy


with open("src/geodaten/city_daten.json", "r", encoding="utf-8") as f:
    city = json.load(f) 

with open("src/geodaten/relation_tags.json", "r", encoding="utf-8") as f:
    streets = json.load(f)


print(city)
print(streets)
bbox = city["Berlin"].values()
list_of_gdf = []



def build_area_query(bbox, streettype):
    """
    tags: Dict wie {"highway": ["motorway", "trunk", ...]}
    """

    south, west, north, east = bbox


    return f"""
    [out:json][timeout:120][bbox:{south},{west},{north},{east}];
    rel[{streettype}];
    out geom;
    """


def parse_osm_result(result):
    data = {"id": [], "highway": [], "name": [], "geometry": []}

    for way in result.ways:
        print(way)
        # if 'highway' in way.tags and way.tags['highway'] == 'primary'
        line = LineString([(node.lon, node.lat) for node in way.nodes])
        data["id"].append(way.id)
        data["highway"].append(way.tags.get("highway"))
        data["name"].append(way.tags.get("name"))
        data["geometry"].append(line)
        # Capture all tags for each way as a dictionary


    # create a GeoDataFrame from the dictionary
    return gpd.GeoDataFrame(data, crs="EPSG:4326").to_crs("EPSG:31468")


api = overpy.Overpass()
def _query_overpass(api,query):
    return api.query(query)


for streettype in street_types_list:

    query = build_area_query(bbox, streettype)
    result = _query_overpass(api, query)
    gdf = parse_osm_result(result)
    
    list_of_gdf.append(gdf)


geodataframe = parse_osm_result(result)
print(geodataframe)
