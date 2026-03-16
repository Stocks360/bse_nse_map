import pandas as pd

# NSE list
nse_url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
nse = pd.read_csv(nse_url)

nse_df = pd.DataFrame({
    "symbol": nse["SYMBOL"],
    "nse": nse["SYMBOL"],
    "bse": "",
    "tradingview": "NSE:" + nse["SYMBOL"],
    "isin": nse["ISIN NUMBER"],
    "company": nse["NAME OF COMPANY"],
    "sector": ""
})

# remove duplicates
nse_df = nse_df.drop_duplicates(subset="symbol")

nse_df.to_csv("bse_nse_map.csv", index=False)

print("Advanced CSV generated")
