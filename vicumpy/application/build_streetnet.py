# application/build_streetnet.py
class BuildStreetNetworkUseCase:

    def __init__(self, query_builder, overpass_client, parser, geo_repo):
        self.query_builder = query_builder
        self.overpass_client = overpass_client
        self.parser = parser
        self.geo_repo = geo_repo

    def execute(self, area_config) -> None:
        """Creates and stores a street network based on the given area configuration.

        This method runs the full pipeline from query creation to fetching,
        parsing, merging and saving the resulting GeoDataFrames.

        Args:
            area_config: Configuration describing the area and street types
                to be included in the street network.

        Raises:
            ValueError: If no GeoDataFrames could be created from the queries.
        """

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
