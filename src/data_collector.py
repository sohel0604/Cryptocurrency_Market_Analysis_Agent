import requests
import pandas as pd
from datetime import datetime

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10, "page": 1}
    data = requests.get(url, params=params).json()
    df = pd.DataFrame(data)[["id", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]
    df["timestamp"] = datetime.now()
    df.to_csv("data/crypto_data.csv", index=False)
    print("✅ Data saved at:", datetime.now())
    return df

if __name__ == "__main__":
    fetch_crypto_data()
