# Configuration settings for Vicumpy

# Example configuration
CONFIG = {
    "api_key": None,  # Set your API key here
    "timeout": 30,    # Request timeout in seconds
    "debug": False,   # Enable debug mode
}


# Name der Stadt, wie er in OSM eingetragen ist
city_name = "Zwickau"

# Ländercode nach ISO3166-1 (z.B. DE, FR, US)
country_code = "DE"

# Admin-Level des Landes (in OSM meist 2 für Länder)
admin_level_country = 2

# Admin-Level der Stadt (in vielen Ländern 8, je nach OSM-Schema)
admin_level_city = 10

# Ob der englische Stadtname verwendet werden soll (name:en statt name)
english_city_name = False


# Abhängig von english_city_name wird in querybuilder.py nameconvention gesetzt
#   False -> "name"
#   True  -> "name:en"
nameconvention = "name"


street_types_list = ["primary", "secondary", "tertiary", "unclassified", "residential"]

# info zu admin_level
# Leipzig = 6           check
# Halle (Saale) = 6     check
# Heidelberg = 6        check
# Leverkusen = 6        check
# Karlsruhe = 6         check
# Kiel = 6              check
# Chemnitz = 6          check
# Fürstenfeldbruck = 8  check
# Ratingen = 8          check
# Neumünster = 6         check
# Landau in der Pfalz = 6 check
# Gießen = 8            check
# München = 6           check
# Hamburg = 4
