
import pandas as pd
from pathlib import Path

path = Path("data/raw")

events = pd.read_parquet("data/processed/events_cleaned.parquet")

p1 = pd.read_csv(path / "item_properties_part1.csv")
p2 = pd.read_csv(path / "item_properties_part2.csv")

properties = pd.concat([p1, p2], ignore_index=True)

event_products = set(events["itemid"].unique())
metadata_products = set(properties["itemid"].unique())

matched = event_products & metadata_products
unmatched = event_products - metadata_products

category_products = set(
    properties.loc[
        properties["property"] == "categoryid", "itemid"
    ].unique()
)

print("Products in events:", len(event_products))
print("Products in metadata:", len(metadata_products))
print("Matched products:", len(matched))
print("Unmatched event products:", len(unmatched))
print("Event products with category:", len(event_products & category_products))
print("Event products without category:", len(event_products - category_products))
