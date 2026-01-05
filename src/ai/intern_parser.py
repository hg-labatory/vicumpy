# vicumpy/ai/intern_parser.py

from src.application.area_config import AreaConfig


class FakeAIIntentParser:
    """
    Very simple rule-based 'fake AI' that converts
    natural language into AreaConfig.
    """

    # erlaubte OSM highway-Werte
    ALLOWED_STREET_TYPES = {
        "motorway": ["motorway", "highway"],
        "car": ["road", "street", "car"],
        "bike": ["bike", "bicycle", "cycle"],
        "foot": ["foot", "pedestrian", "walk"],
    }

    STREET_TYPE_MAPPING = {
        "motorway": ["motorway", "trunk"],
        "car": ["primary", "secondary", "tertiary", "residential"],
        "bike": ["cycleway", "path"],
        "foot": ["footway", "pedestrian", "path", "steps"],
    }

    def parse(self, text: str) -> AreaConfig:
        text_lower = text.lower()

        street_types = set()

        """Wenn irgendein Keyword einer Kategorie im Text vorkommt,
        dann werden alle OSM-Straßentypen, die zu dieser Kategorie gehören,
        zu street_types hinzugefügt."""
        for category, keywords in self.ALLOWED_STREET_TYPES.items():
            if any(word in text_lower for word in keywords):
                street_types.update(self.STREET_TYPE_MAPPING[category])

        if not street_types:
            raise ValueError("Could not detect any street types from text")

        # sehr einfache Stadt-Erkennung (für Fake-KI ok)
        city = self._extract_city(text)
        return AreaConfig(
            street_types=list(street_types),
            city_name=city,
            country_code="DE",
            admin_level_country=2,
            admin_level_city=4,
            nameconvention="name",
        )

    def _extract_city(self, text: str) -> str:
        # Fake: letztes Wort mit Großbuchstaben
        words = text.split()
        for word in reversed(words):
            if word[0].isupper():
                return word

        raise ValueError("Could not detect city name")
