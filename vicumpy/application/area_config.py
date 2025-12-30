# application/area_config.py
from dataclasses import dataclass


@dataclass(frozen=True)
class AreaConfig:
    street_types: list[str]
    country_code: str
    admin_level_country: int
    city_name: str
    admin_level_city: int
    nameconvention: str

