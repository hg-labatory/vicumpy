# infrastructure/osm_parser.py

from shapely import LineString


class ResultParser:

    def parse(self, result):
        records = {"id": [], "highway": [], "name": [], "geometry": []}

        for way in result.ways:
            line = LineString([(p.lon, p.lat) for p in way.nodes])

            records["id"].append(way.id)
            records["highway"].append(way.tags.get("highway"))
            records["name"].append(way.tags.get("name"))
            records["geometry"].append(line)

        return records
