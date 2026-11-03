import logging
import pandas as pd


logging.basicConfig(filename = "automation.log",level=logging.INFO,format = "%(asctime)s - %(levelname)s - %(message)s ")

try:
    data = pd.read_excel("test_folder/Spreadsheets/nothing.xlsx")
except FileNotFoundError:
    logging.error("Input file not found")
    raise SystemExit("File not found. See automation.log")

rows_in = len(data)
data.columns = data.columns.str.strip().str.lower()
data = data.drop_duplicates()    

data["quantity"]  = pd.to_numeric(data["quantity"], errors="coerce")
data["price"]  = pd.to_numeric(data["price"], errors="coerce")

bad = data[data["quantity"].isna() | data["price"].isna()]
print("rows with bad numbers")
print(bad)

good = data.drop(bad.index)

good = good.copy()
good["quantity"] = good["quantity"].astype(int)

good.to_excel("clean_sales.xlsx", index=False)
bad.to_excel("rejected_rows.xlsx", index=False)

logging.info("Read %d rows, kept %d, rejected %d", rows_in, len(good), len(bad))
print("Done. Kept", len(good), "rows, rejected", len(bad))