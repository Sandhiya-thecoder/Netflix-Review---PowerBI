"""
data_generator.py
-----------------
Generates a synthetic Netflix dataset matching the structure of netflix_customer_reviews.xlsx.
Useful for Power BI projects and data visualization demos.

"""

import random
import pandas as pd
from faker import Faker
from datetime import datetime
import os

# Initialize Faker
fake = Faker()

# Configuration
NUM_SHOWS = 5000  # number of rows to generate
OUTPUT_FILE = "netflix_customer_reviews_generated.xlsx"

# Data pools
content_types = ["Movie", "TV Show"]
ratings = ["G", "PG", "PG-13", "R", "NC-17", "TV-MA", "TV-14", "TV-PG", "TV-Y", "TV-Y7"]
genres = [
    "Drama", "Action", "Comedy", "Thriller", "Romance",
    "Horror", "Documentary", "Sci-Fi", "Fantasy", "Adventure"
]
countries = [
    "United States", "India", "United Kingdom", "Canada", "Australia",
    "Germany", "France", "Japan", "Brazil", "South Korea", "Mexico"
]

# Helper functions
def random_duration(content_type):
    if content_type == "Movie":
        return f"{random.randint(60, 180)} min"
    else:
        return f"{random.randint(1, 10)} Seasons"

def random_genres():
    return ", ".join(random.sample(genres, random.randint(1, 3)))

def generate_fake_cast():
    return ", ".join([fake.name() for _ in range(random.randint(2, 5))])

# Main generator
def generate_dataset():
    records = []

    for i in range(1, NUM_SHOWS + 1):
        ctype = random.choice(content_types)
        record = {
            "show_id": i,
            "type": ctype,
            "title": fake.catch_phrase(),
            "director": fake.name(),
            "cast": generate_fake_cast(),
            "country": random.choice(countries),
            "date_added": fake.date_between(start_date="-3y", end_date="today").strftime("%B %d, %Y"),
            "released_year": random.randint(1990, 2024),
            "rating": random.choice(ratings),
            "duration": random_duration(ctype),
            "listed_in": random_genres(),
            "description": fake.text(max_nb_chars=150)
        }
        records.append(record)

    df = pd.DataFrame(records)
    return df


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    df = generate_dataset()
    output_path = os.path.join("data", OUTPUT_FILE)
    df.to_excel(output_path, index=False)

    print(f"Synthetic Netflix dataset generated successfully!")
    print(f"File saved to: {output_path}")
    print(f"Total records: {len(df)}")
