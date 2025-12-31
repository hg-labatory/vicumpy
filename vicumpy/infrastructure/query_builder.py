class QueryBuilder:

    def build_queries(self, config):

        queries = []

        for streettype in config.street_types:


            query = f"""area["ISO3166-1"={config.country_code}][admin_level={config.admin_level_country}]->.country;
            area[{config.nameconvention}={config.city_name}][admin_level={config.admin_level_city}]->.city;
            way[highway={streettype}](area.city)(area.country);
            (._;>;);
            out body;
            """
            queries.append(query)

        return queries
