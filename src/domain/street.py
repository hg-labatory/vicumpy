# domain/street.py
from dataclasses import dataclass
from typing import Any


@dataclass
class Street:
    id: int
    name: str | None
    street_type: str
    geometry: Any  # bewusst generisch!



class StreetNetwork:
    def __init__(self, streets: list[Street]):
        self.streets = streets

    def filter_by_type(self, street_type: str) -> "StreetNetwork":
        return StreetNetwork([s for s in self.streets if s.street_type == street_type])

    def __len__(self) -> int:
        return len(self.streets)
    
    def to_records(self) -> dict[str, list[Any]]:
        records = {"id": [], "highway": [], "name": [], "geometry": []}
        for street in self.streets:
            records["id"].append(street.id)
            records["highway"].append(street.street_type)
            records["name"].append(street.name)
            records["geometry"].append(street.geometry)
        return records
