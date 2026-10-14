import pandas as pd
import matplotlib.pyplot as plt 

data  = pd.read_csv("test_folder/Spreadsheets/sales.csv")

data["revenue"] = data["quantity"]*data["price"]

print("Total revenue:", round(data["revenue"].sum(),2))

by_product = data.groupby("product")["revenue"].sum()
print(by_product.sort_values(ascending=False))


by_product = by_product.sort_values(ascending=False)

by_product.plot(kind ="bar", title = "Revenue by product" )
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_chart.png")

plt.clf()

by_product = by_product.round(2)
by_product.to_csv("revenue_by_product.csv")
print("Report Saved")


by_date = data.groupby("date")["revenue"].sum().round(2)
print(by_date)

by_date.plot(kind = "line",title  ="Revenue by date", marker="o")
plt.ylabel("Revenue")
plt.tight_layout()
marker="o"

plt.savefig("revenue_by_date.png")

by_date = by_date.round(2)
by_date.to_csv("revenue_by_date.csv")