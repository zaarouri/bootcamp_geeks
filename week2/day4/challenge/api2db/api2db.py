

import os
import random
import requests
import psycopg2


# ──────────────────────────────────────────────────────────────────────────
# Database helpers
# ──────────────────────────────────────────────────────────────────────────
def get_connection():
    return psycopg2.connect(
        host= "localhost",
        port="5432",
        dbname="countries",
        user="postgres",
        password="postgres"
    )


def create_table(cur):
    """Create the target table if it doesn't exist."""
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS countries (
            id         SERIAL PRIMARY KEY,
            name       TEXT,
            capital    TEXT,
            flag       TEXT,
            subregion  TEXT,
            population BIGINT
        );
        """
    )


# ──────────────────────────────────────────────────────────────────────────
# Data fetch & transform
# ──────────────────────────────────────────────────────────────────────────
API_FIELDS = "name,capital,flags,subregion,population"
API_URL = f"https://restcountries.com/v3.1/all?fields={API_FIELDS}"


def fetch_random_countries(n: int = 10):
    """Return *n* random country payloads from REST Countries."""
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()
    all_countries = response.json()
    return random.sample(all_countries, n)


def flatten(country):
    """Convert the REST Countries JSON object into a simple tuple."""
    return (
        country.get("name", {}).get("common"),           # name
        (country.get("capital") or [None])[0],           # capital
        country.get("flags", {}).get("png")
        or country.get("flags", {}).get("svg"),          # flag URL
        country.get("subregion"),                        # sub-region
        country.get("population"),                       # population
    )


# ──────────────────────────────────────────────────────────────────────────
# Main routine
# ──────────────────────────────────────────────────────────────────────────
def main():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                create_table(cur)
                conn.commit()
                
                records = [flatten(c) for c in fetch_random_countries()]

                # 3) Insert them
                insert_sql = """
                    INSERT INTO countries (name, capital, flag, subregion, population)
                    VALUES (%s, %s, %s, %s, %s)
                """
                for row in records:
                    cur.execute(insert_sql, row)
                conn.commit()

                print(f"Inserted {len(records)} countries into 'countries' table.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
