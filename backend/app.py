import sqlite3


from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Geography Game API is running!"

@app.route("/api/message")
def message():
    return jsonify({
        "message": "Hello from Flask!"
    })


@app.route("/api/countries/random")
def random_country():
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
        ORDER BY RANDOM()
        LIMIT 1
    """)

    country = cursor.fetchone()
    connection.close()

    return jsonify({
        "name": country[0],
        "code": country[1],
        "ranks": {
            "population": country[2],
            "area": country[3],
            "gdp_per_capita": country[4],
            "tourism": country[5],
            "fertility": country[6],
            "life_expectancy": country[7],
            "emissions_per_capita": country[8],
            "cuisine": country[9],
            "internet_usage": country[10]
        }
    })



if __name__ == "__main__":
    app.run(debug=True)