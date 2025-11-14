#  Multi-Crypto, Multi-Currency Price Tracker

This Python project fetches **live cryptocurrency prices** for Bitcoin (BTC), Ethereum (ETH), and Dogecoin (DOGE)  
in **USD, GBP, and EUR** using the CoinGecko API.  
It saves the results to a CSV file, plots the **BTC (USD) trend**, and even includes a **price-change alert system** .

---

##  Features

 Fetches live prices for BTC, ETH, and DOGE  
 Tracks values in USD, GBP, and EUR  
 Detects sudden Bitcoin price drops/rises (±2%)  
 Saves clean CSV file (`crypto_prices.csv`)  
 Generates a Bitcoin price trend graph (`bitcoin_price_graph.png`)  
 Runs automatically every 10 seconds × 10 fetches  

---

##  Technologies Used

- **Python 3**
- **Requests** – API calls  
- **Pandas** – Data handling and CSV saving  
- **Matplotlib** – Graph plotting  
- **Datetime / Time** – Timestamping and scheduling  

---

##  Project Files

| File | Description |
|------|--------------|
| `crypto_price_tracker.py` | Main Python script |
| `crypto_prices.csv` | Sample generated CSV |
| `bitcoin_price_graph.png` | BTC price trend graph |
| `README.md` | Project documentation |


---

## 🚀 How to Run

1. **Clone or download** the repository  
   ```bash
   git clone https://github.com/yourusername/Multi_Crypto_Price_Tracker.git
   cd Multi_Crypto_Price_Tracker

2. **Install dependencies**
pip install -r requirements.txt

3. **Run the script**
python crypto_price_tracker.py

4. **The script will:**
.Fetch data every 10 seconds (10 times total)
.Save it in crypto_prices.csv
.Generate a graph bitcoin_price_graph.png

5. **Example Output**
1/10 | 2025-11-12 19:30:01
BTC → USD: 68900, GBP: 56500, EUR: 63500
ETH → USD: 3120, GBP: 2550, EUR: 2880
DOGE → USD: 0.118, GBP: 0.097, EUR: 0.109
------------------------------------------------------------
INFO: Bitcoin rose 2.45% since last reading.

6. **Real-World Use Cases**

.Track cryptocurrency trends in real-time
.Automate alert systems for BTC price fluctuations
.Build dashboards or daily summary reports
.Extend for email or Telegram notifications

**Author**
👨‍💻 Reister
Python Automation & Data Developer
📧 yunusshaikhy2006@gmail.com