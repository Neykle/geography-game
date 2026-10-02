import csv
import sqlite3

connection = sqlite3.connect("geography.db")
cursor = connection.cursor()

with open("../data/country_stats.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Find the country ID using the country code
        cursor.execute(
            "SELECT id FROM countries WHERE code = ?",
            (row["code"],)
        )

        country = cursor.fetchone()

        if country is None:
            print(f'Country not found: {row["code"]}')
            continue

        country_id = country[0]

        cursor.execute("""
            INSERT INTO country_stats (
                country_id,
                population_rank,
                area_rank,
                gdp_per_capita_rank,
                tourism_rank,
                fertility_rank,
                life_expectancy_rank,
                emissions_per_capita_rank,
                cuisine_rank,
                internet_usage_rank
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            country_id,
            row["population_rank"],
            row["area_rank"],
            row["gdp_per_capita_rank"],
            row["tourism_rank"],
            row["fertility_rank"],
            row["life_expectancy_rank"],
            row["emissions_per_capita_rank"],
            row["cuisine_rank"],
            row["internet_usage_rank"]
        ))

connection.commit()
connection.close()

print("Country stats imported successfully!")