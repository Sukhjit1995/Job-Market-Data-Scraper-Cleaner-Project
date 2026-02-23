import os
import requests
import json
from dotenv import load_dotenv
import pandas as pd



# Load environment variables
load_dotenv(dotenv_path=".env")

APP_ID = os.getenv("APP_ID_")
APP_KEY = os.getenv("APP_KEY_")
print("APP_ID:", APP_ID)
print("APP_KEY:", APP_KEY)

# Define API endpoint
url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"

# Define parameters
params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 20,
    "what": "data analyst",
    "content-type": "application/json"
}

# Make request
response = requests.get(url, params=params)

# Check status
if response.status_code == 200:
    data = response.json()
    print("API call successful")

    # Save raw JSON
    with open("data/new_raw_jobs.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Raw data saved successfully")

else:
    print(f"Error: {response.status_code}")
    print(response.status_code)
    print(response.text)



