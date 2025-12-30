# application/build_streetnet.py
class BuildStreetNetworkUseCase:

    def __init__(self, query_builder, overpass_client, parser, geo_repo):
        self.query_builder = query_builder
        self.overpass_client = overpass_client
        self.parser = parser
        self.geo_repo = geo_repo

    def execute(self, area_config):

        queries = self.query_builder.build_queries(area_config)

        gdfs = []

        for query in queries:
            raw_result = self.overpass_client.fetch(query)
            records = self.parser.parse(raw_result)
            gdf = self.geo_repo.create_gdf(records)
            gdfs.append(gdf)

        if not gdfs:
            raise ValueError("No GeoDataFrames created")

        merged = self.geo_repo.concat(gdfs)
        self.geo_repo.save(merged)
