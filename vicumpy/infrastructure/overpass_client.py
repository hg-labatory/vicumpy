# infrastructure/overpass_client.py
import overpy


class OverpassClient:
    def __init__(self, url:str="https://overpass.kumi.systems/api/interpreter"):

        self.api = overpy.Overpass(url =url)

    def fetch(self, query: str):
        return self.api.query(query)
    
