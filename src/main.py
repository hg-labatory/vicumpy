import sys
from src.application.build_streetnet import BuildStreetNetworkUseCase
from src.ai.intern_parser import FakeAIIntentParser
from src.infrastructure.osm_parser import ResultParser
from src.infrastructure.overpass_client import OverpassClient
from src.infrastructure.query_builder import QueryBuilder
from src.infrastructure.geopackage_repository import GeopackageRepository


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
