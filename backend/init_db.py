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

connection.commit()
connection.close()

print("Database created successfully!")