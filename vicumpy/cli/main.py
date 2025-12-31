import sys
from vicumpy.application.area_config import AreaConfig
from vicumpy.application.build_streetnet import BuildStreetNetworkUseCase

from vicumpy.ai.intern_parser import FakeAIIntentParser

from vicumpy.infrastructure.osm_parser import ResultParser
from vicumpy.infrastructure.overpass_client import OverpassClient
from vicumpy.infrastructure.query_builder import QueryBuilder
from vicumpy.infrastructure.geopackage_repository import GeopackageRepository
from vicumpy.application.area_config import AreaConfig


def main():

    user_text = " ".join(sys.argv[1:])  # Kommandozeilenargumente zu einem String verbinden
    if not user_text:
        raise ValueError("Please provide a description of the area as a command line argument.")
    ai_parser = FakeAIIntentParser()
    area_config = ai_parser.parse(user_text)
    print(area_config)
    use_case = BuildStreetNetworkUseCase(
        query_builder=QueryBuilder(),
        overpass_client=OverpassClient(),
        parser=ResultParser(),
        geo_repo=GeopackageRepository("streetnet.gpkg"),
    )
    use_case.execute(area_config)


if __name__ == "__main__":
    main()
