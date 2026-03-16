import pandas as pd

# NSE stock list
url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

df = pd.read_csv(url)

# create TradingView symbol
df["tradingview"] = "NSE:" + df["SYMBOL"]

# build output CSV
out = pd.DataFrame({
    "symbol": df["SYMBOL"],
    "nse": df["SYMBOL"],
    "bse": "",
    "tradingview": df["tradingview"]
})

# save CSV
out.to_csv("bse_nse_map.csv", index=False)

print("CSV updated successfully")
