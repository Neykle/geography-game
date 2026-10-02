import csv
import sqlite3

connection = sqlite3.connect("geography.db")
cursor = connection.cursor()

with open("../data/countries.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
            INSERT OR IGNORE INTO countries (name, code)
            VALUES (?, ?)
        """, (row["name"], row["code"]))

connection.commit()
connection.close()

print("Countries imported successfully!")