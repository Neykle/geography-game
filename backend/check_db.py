import sqlite3

connection = sqlite3.connect("geography.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT
        countries.name,
        countries.code,
        country_stats.population_rank,
        country_stats.area_rank,
        country_stats.gdp_per_capita_rank,
        country_stats.tourism_rank,
        country_stats.fertility_rank,
        country_stats.life_expectancy_rank,
        country_stats.emissions_per_capita_rank,
        country_stats.cuisine_rank,
        country_stats.internet_usage_rank
    FROM country_stats
    JOIN countries
        ON country_stats.country_id = countries.id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

    if None in row:
        print("WARNING: missing data!")

print("Total stats rows:", len(rows))

connection.close()