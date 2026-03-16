import pandas as pd

# -------- NSE STOCK LIST --------
nse_url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
nse = pd.read_csv(nse_url)

nse_df = pd.DataFrame({
    "symbol": nse["SYMBOL"],
    "nse": nse["SYMBOL"],
    "bse": "",
    "tradingview": "NSE:" + nse["SYMBOL"],
    "company": nse["NAME OF COMPANY"]
})

# -------- BSE STOCK LIST --------
try:
    bse_url = "https://www.bseindia.com/download/BhavCopy/Equity/EQ_ISINCODE_20240101.csv"
    bse = pd.read_csv(bse_url)

    bse_df = pd.DataFrame({
        "symbol": bse["SC_CODE"].astype(str),
        "nse": "",
        "bse": bse["SC_CODE"],
        "tradingview": "BSE:" + bse["SC_CODE"].astype(str),
        "company": bse["SC_NAME"]
    })
except:
    bse_df = pd.DataFrame()

# -------- COMBINE --------
combined = pd.concat([nse_df, bse_df], ignore_index=True)

combined = combined.drop_duplicates(subset="symbol")

combined.to_csv("bse_nse_map.csv", index=False)

print("CSV updated with NSE + BSE stocks")
