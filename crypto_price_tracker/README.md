# Crypto Price Alert Bot

This Python project fetches live cryptocurrency prices for Bitcoin (BTC), Ethereum (ETH), and Dogecoin (DOGE) in USD, GBP, and EUR using the CoinGecko API.  
It saves the data to a CSV file, plots the BTC (USD) price trend, and includes a price-change alert system.

---

##  Features

- Fetches live prices for BTC, ETH, and DOGE  
- Tracks prices in USD, GBP, and EUR  
- Detects sudden Bitcoin price changes (±2%)  
- Saves data to CSV file (`crypto_prices_alert.csv`)  
- Generates Bitcoin price trend graph (`bitcoin_price_alert_graph.png`)  
- Runs automatically every 10 seconds  

---

##  Technologies Used

- Python 3  
- Requests – API calls  
- Pandas – Data handling and CSV saving  
- Matplotlib – Graph plotting  
- Datetime / Time – Timestamping and scheduling  

---

##  Project Files

| File | Description |
|------|--------------|
| `crypto_price_tracker.py` | Main Python script |
| `crypto_prices_alert.csv` | Generated CSV file |
| `bitcoin_price_alert_graph.png` | BTC price trend graph |
| `README.md` | Project documentation |

---

##  How to Run

1. Clone the repository  


##  How to Run

1. **Clone or download** the repository  
   ```bash
   git clone https://github.com/yourusername/crypto_price_alert.py
   cd crypto_price_alert.py

2. **Install dependencies**
pip install -r requirements.txt

3. **Run the script**
python crypto_price_tracker.py


4. The script will:
- Fetch prices every 10 seconds  
- Save data to CSV  
- Generate price trend graph  
- Show alerts in terminal  

---

##  Example Output

1/5 | 2025-11-12 19:30:01
BTC → USD: 68900, GBP: 56500, EUR: 63500
ETH → USD: 3120, GBP: 2550, EUR: 2880
DOGE → USD: 0.118, GBP: 0.097, EUR: 0.109

INFO: Bitcoin rose 2.45% since last reading.

6. **Real-World Use Cases**

---

##  Real-World Use Cases

- Track cryptocurrency trends in real-time  
- Build automated alert systems  
- Generate daily price reports  
- Extend to email / Telegram notifications  

---

##  Author

Reister  
Python Automation & Data Developer  
