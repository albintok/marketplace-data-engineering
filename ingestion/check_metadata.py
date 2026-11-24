
import pandas as pd
from pathlib import Path

path = Path("data/raw")

p1 = pd.read_csv(path / "item_properties_part1.csv")
p2 = pd.read_csv(path / "item_properties_part2.csv")
cat = pd.read_csv(path / "category_tree.csv")

properties = pd.concat([p1, p2], ignore_index=True)

print("\n1. Property distribution:")
print(properties["property"].value_counts().head(15))

print("\n2. Category ID records in properties:")
print((properties["property"] == "categoryid").sum())

print("\n3. Duplicate property records:")
print(properties.duplicated().sum())

print("\n4. Category roots (missing parent):")
print(cat[cat["parentid"].isna()].head(10))

print("\n5. Products with properties:")
print(properties["itemid"].nunique())

print("\n6. Products in events:")
events = pd.read_parquet("data/processed/events_cleaned.parquet")
print(events["itemid"].nunique())
