#!.venv\Scripts\python.exe

import requests
from config import city_dic
import logging
import json



def _fetch_nominatim_data(url: str, headers: dict, city_name: str) -> dict | None:
    """Fetch data from Nominatim API and handle response validation.
    
    :param url: The request URL
    :param headers: Request headers
    :param city_name: Name of the city for logging
    :return: Parsed JSON data or None if request failed
    """
    response = requests.get(url, headers=headers, timeout=10)
    logging.debug("HTTP status code: %s", response.status_code)

    if response.status_code != 200:
        logging.warning(
            "No data found for city: %s, status: %s",
            city_name,
            response.status_code,
        )
        return None

    json_data = response.json()
    if not json_data:
        logging.warning("Empty JSON result for city: %s", city_name)
        return None

    return json_data

def get_city_bbox(city_name: str):
    """
    Fetch the bounding box for a given city and store raw data in city_dic.

    :param city_name: Name of the city
    :return: Dictionary with bbox coordinates or None if not found/invalid
    """
    logging.info("Starting to fetch bbox for city: %s", city_name)

    url = (
        "https://nominatim.openstreetmap.org/search"
        f"?q={city_name}"
        "&format=json"
        "&limit=1"
    )
    logging.debug("Request URL: %s", url)

    # Nominatim verlangt einen sprechenden
    headers = {"User-Agent": "my-app/0.0.1"}

    try:
        json_data = _fetch_nominatim_data(url, headers, city_name)
        if json_data is None:
            return None

        data = json_data[0]
        return _parse_bbox_from_result(data, city_name)
    except Exception:
        logging.exception("Error fetching bbox for city: %s", city_name)
        return None

def _parse_bbox_from_result(data: dict, city_name: str) -> dict | None:
    """Extract bbox from a Nominatim result dict and store raw data."""
    bbox_raw = data.get("boundingbox")
    if not bbox_raw or len(bbox_raw) != 4:
        logging.warning("Invalid boundingbox data for city: %s", city_name)
        return None

    bbox = {
        "min_lat": float(bbox_raw[0]),
        "max_lat": float(bbox_raw[1]),
        "min_lon": float(bbox_raw[2]),
        "max_lon": float(bbox_raw[3]),
    }


    TODO: "Fill in the code to write the data to src/geodaten/data.json" 

    with open("src/geodaten/city_daten.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=False))

    logging.info("Successfully fetched bbox for %s: %s", city_name, bbox)
    return bbox

city_dic["Stadt"] = get_city_bbox(city_dic.keys())
