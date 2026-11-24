
import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw")

# Load product metadata
properties1 = pd.read_csv(DATA_PATH / "item_properties_part1.csv")
properties2 = pd.read_csv(DATA_PATH / "item_properties_part2.csv")
categories = pd.read_csv(DATA_PATH / "category_tree.csv")

print("\n===== ITEM PROPERTIES PART 1 =====")
print(properties1.shape)
print(properties1.head())
print(properties1.isnull().sum())

print("\n===== ITEM PROPERTIES PART 2 =====")
print(properties2.shape)
print(properties2.head())
print(properties2.isnull().sum())

print("\n===== CATEGORY TREE =====")
print(categories.shape)
print(categories.head())
print(categories.isnull().sum())

print("\nUnique products in properties:")
print(pd.concat([
    properties1["itemid"],
    properties2["itemid"]
]).nunique())

print("\nUnique categories:")
print(categories["categoryid"].nunique())
