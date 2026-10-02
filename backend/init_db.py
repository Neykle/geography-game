import sqlite3

connection = sqlite3.connect("geography.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        code TEXT UNIQUE NOT NULL
    )
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS country_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_id INTEGER NOT NULL,
        population_rank INTEGER,
        area_rank INTEGER,
        gdp_per_capita_rank INTEGER,
        tourism_rank INTEGER,
        fertility_rank INTEGER,
        life_expectancy_rank INTEGER,
        emissions_per_capita_rank INTEGER,
        cuisine_rank INTEGER,
        internet_usage_rank INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )
""")


connection.commit()
connection.close()

print("Database created successfully!") 