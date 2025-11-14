"""
 Multi-Crypto, Multi-Currency Price Tracker
Fetches live prices for Bitcoin, Ethereum, and Dogecoin in USD, GBP, and EUR.
Saves data to CSV and plots BTC(USD) trend.

Author: Reister
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime

# --- API URL ---
URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin&vs_currencies=usd,gbp,eur"

# --- Empty list to store fetched prices ---
records = []

# --- Fetch price 5 times (every 10 seconds) ---
for i in range(10):
    try:
        response = requests.get(URL)
        data = response.json()

        # Extract prices for each coin and currency
        btc_usd = data["bitcoin"]["usd"]
        btc_gbp = data["bitcoin"]["gbp"]
        btc_eur = data["bitcoin"]["eur"]

        eth_usd = data["ethereum"]["usd"]
        eth_gbp = data["ethereum"]["gbp"]
        eth_eur = data["ethereum"]["eur"]

        doge_usd = data["dogecoin"]["usd"]
        doge_gbp = data["dogecoin"]["gbp"]
        doge_eur = data["dogecoin"]["eur"]

        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Store record
        records.append({
            "Time": time_now,
            "BTC (USD)": btc_usd, "BTC (GBP)": btc_gbp, "BTC (EUR)": btc_eur,
            "ETH (USD)": eth_usd, "ETH (GBP)": eth_gbp, "ETH (EUR)": eth_eur,
            "DOGE (USD)": doge_usd, "DOGE (GBP)": doge_gbp, "DOGE (EUR)": doge_eur
        })

        # Print live prices
        print(f"{i+1}/10 | {time_now}")
        print(f"BTC → USD: {btc_usd}, GBP: {btc_gbp}, EUR: {btc_eur}")
        print(f"ETH → USD: {eth_usd}, GBP: {eth_gbp}, EUR: {eth_eur}")
        print(f"DOGE → USD: {doge_usd}, GBP: {doge_gbp}, EUR: {doge_eur}")

        # ---  Price Drop Alert (BTC > 2% drop) ---
        if len(records) > 1:
            prev_btc = records[-2]["BTC (USD)"]
            change = ((btc_usd - prev_btc) / prev_btc) * 100
            if change <= -2:
                print(f" ALERT: Bitcoin dropped {abs(change):.2f}% from last reading!")
            elif change >= 2:
                print(f" INFO: Bitcoin rose {change:.2f}% since last reading.")

        print("-" * 60)
        time.sleep(10) # wait 10 sec between updates

    except Exception as e:
        print(" Error fetching data:", e)
        time.sleep(10)

# --- Convert to DataFrame & Save to CSV ---
df = pd.DataFrame(records)
df.to_csv("crypto_prices_alert.csv", index=False)
print("\n Data saved to crypto_prices_alert.csv")

# --- Plot Graph (BTC-USD trend) ---
plt.figure(figsize=(10, 5))
plt.plot(df["Time"], df["BTC (USD)"], marker="o", color="tab:blue", label="BTC (USD)")
plt.xticks(rotation=45)
plt.title("Bitcoin Price (USD) Over Time", color="darkred", fontweight="bold")
plt.xlabel("Time")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.savefig("bitcoin_price_alert_graph.png")
print(" Graph saved as bitcoin_price_alert_graph.png")
plt.show()
