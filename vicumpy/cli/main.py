from vicumpy.application.area_config import AreaConfig
from vicumpy.application.build_streetnet import BuildStreetNetworkUseCase
from vicumpy.config.settings import country_code, admin_level_country, city_name, nameconvention, street_types, admin_level_city

from vicumpy.infrastructure.osm_parser import ResultParser
from vicumpy.infrastructure.overpass_client import OverpassClient
from vicumpy.infrastructure.query_builder import QueryBuilder
from vicumpy.infrastructure.geopackage_repository import GeopackageRepository
from vicumpy.application.area_config import AreaConfig

area_config = AreaConfig(
    street_types=street_types,
    country_code=country_code,
    admin_level_country=admin_level_country,
    city_name=city_name,
    admin_level_city=admin_level_city,
    nameconvention=nameconvention,
)
print(area_config)
use_case = BuildStreetNetworkUseCase(
    query_builder=QueryBuilder(),
    overpass_client=OverpassClient(),
    parser=ResultParser(),
    geo_repo=GeopackageRepository("streetnet.gpkg"),
)


use_case.execute(area_config)
