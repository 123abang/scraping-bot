import time
import requests
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()             
API_KEY = os.getenv("API_KEY")
TEXT_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
DETAILS_URL     = "https://maps.googleapis.com/maps/api/place/details/json"

def fetch_logistics_companies(
    query="logistics company",
    region="uk",         # bias results to the UK
    max_pages=3,         # Google returns up to 3 pages of 20 results each
    pause_between=2.0    # wait time before using next_page_token
):
    companies = []
    params = {
        "query": query,
        "region": region,
        "key": API_KEY
    }

    for _ in range(max_pages):
        resp = requests.get(TEXT_SEARCH_URL, params=params)
        resp.raise_for_status()
        data = resp.json()

        for place in data.get("results", []):
            pid = place["place_id"]
            # fetch detailed contact info
            dresp = requests.get(DETAILS_URL, params={
                "place_id": pid,
                "fields": "name,formatted_address,formatted_phone_number,website",
                "key": API_KEY
            })
            dresp.raise_for_status()
            detail = dresp.json().get("result", {})
            companies.append({
                "name":    detail.get("name", ""),
                "address": detail.get("formatted_address", ""),
                "phone":   detail.get("formatted_phone_number", ""),
                "website": detail.get("website", "")
            })

        # paginate
        token = data.get("next_page_token")
        if not token:
            break
        time.sleep(pause_between)
        params = {"pagetoken": token, "key": API_KEY}

    return pd.DataFrame(companies)


if __name__ == "__main__":
    df = fetch_logistics_companies()
    print(f"Fetched {len(df)} companies")
    df.to_csv("uk_logistics_companies.csv", index=False)
    print("Saved to uk_logistics_companies.csv")
