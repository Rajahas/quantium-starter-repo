import pandas as pd

df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

combined_df = pd.concat([df0, df1, df2], ignore_index=True)

pink_df = combined_df[
    combined_df["product"].str.contains("pink", case=False, na=False)
].copy()

pink_df["price"] = (
    pink_df["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .astype(float)
)

pink_df["sales"] = pink_df["quantity"] * pink_df["price"]

final_df = pink_df[["sales", "date", "region"]]

final_df.to_csv("data/processed_sales_data.csv", index=False)

print("Data processing complete.")
print("Rows written:", len(final_df))
print(final_df.head())