#!.venv\Scripts\python.exe
# Module to fetch road network data
import json
import requests
from config import CONFIG, street_types_list
import overpass


def get_road_network(bbox):
    """
    Fetch road network data within a bounding box.

    :param bbox: Dictionary with min_lat, max_lat, min_lon, max_lon
    :return: Road network data or None if failed
    """
    # Placeholder implementation - replace with actual API call
    # Example: Use Overpass API for OpenStreetMap data
    query = f"""
    [out:json];
    (
      way["highway"]({bbox['min_lat']},{bbox['min_lon']},{bbox['max_lat']},{bbox['max_lon']});
    );
    out geom;
    """
    url = "https://overpass-api.de/api/interpreter"
    response = requests.post(url, data={"data": query}, timeout=CONFIG["timeout"])
    return response.json() if response.status_code == 200 else None


with open("src/geodaten/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


print(data)

response = get_road_network(data["Berlin"])
print(response)
