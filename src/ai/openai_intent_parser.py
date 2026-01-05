#! .venv\Scripts\python.exe
import json
from openai import OpenAI
from application.area_config import AreaConfig
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")


class OpenAIIntentParser:

    def __init__(self, api_key=api_key):
        self.client = OpenAI(api_key=api_key)

    def parse(self, text: str) -> AreaConfig:
        response = self.client.responses.create(
            model="gpt-4o-mini",
            input=[
                {
                    "role": "system",
                    "content": (
                        "You convert user requests into structured OpenStreetMap parameters.\n"
                        "Allowed highway values:\n"
                        "motorway, trunk, primary, secondary, tertiary,\n"
                        "residential, unclassified, service,\n"
                        "cycleway, footway, pedestrian, path, steps, living_street\n\n"
                        "Return ONLY valid JSON."
                    ),
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
        )

        content = response.output_text
        data = json.loads(content)

        return AreaConfig(
            street_types=data["street_types"],
            city_name=data["city_name"],
            country_code=data.get("country_code", "DE"),
            admin_level_country=2,
            admin_level_city=8,
            nameconvention="name",
        )


ai = OpenAIIntentParser().parse("I want to download all residential and primary roads in Berlin, Germany.")
