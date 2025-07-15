📈 Live Stock Tracker
======================

A simple and live stock market price tracker built with Python using the `yfinance` library.

🔍 What It Does
---------------
- Allows you to enter stock symbols (e.g., AAPL, TSLA, MSFT)
- Fetches and displays live price, % change, daily high & low
- Updates prices at your chosen interval
- Logs all data into a CSV file (`stock_data.csv`) for later review

🛠 Requirements
---------------
- Python 3.x
- Install yfinance:
    pip install yfinance

📦 Optional (for better formatting):
- Run in a terminal or console that supports emojis (📈, 🔁, 🛑 etc.)

🚀 How to Use
-------------
1. Clone or download this repository.
2. Open a terminal in the directory.
3. Run the script:
    python stock_tracker.py

4. Enter stock symbols separated by commas (e.g., AAPL, TSLA, MSFT)
5. Enter how often you want it to refresh (in seconds).
6. Press `Ctrl + C` to stop tracking.

📄 Output CSV
-------------
Each tracked update is logged into `stock_data.csv` with:
- Symbol
- Current price
- % Change
- Day's High and Low
- Timestamp

⚠️ Note: The CSV currently rewrites the header row every time. This may lead to duplicate headers in the file.

📁 Files
--------
- `stock_tracker.py` — Main Python script
- `stock_data.csv` — Automatically created log file
- `README.txt` — You're reading it!

🧑‍💻 Made by Arib
------------------------
Happy tracking! 📊🚀
