
import pandas as pd
from pathlib import Path

# File locations
RAW_PATH = Path("data/raw/events.csv")
OUTPUT_PATH = Path("data/processed/events_cleaned.parquet")

# Load raw data
events = pd.read_csv(RAW_PATH)

print("Original records:", len(events))

# Remove exact duplicate rows
events = events.drop_duplicates()

# Convert timestamp from milliseconds to datetime
events["timestamp"] = pd.to_datetime(
    events["timestamp"], unit="ms"
)

# Validate event types
valid_events = ["view", "addtocart", "transaction"]

events = events[events["event"].isin(valid_events)]

# Save cleaned data
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
events.to_parquet(OUTPUT_PATH, index=False)

print("Cleaned records:", len(events))
print("Duplicates removed:", len(pd.read_csv(RAW_PATH)) - len(events))
print("Remaining duplicates:", events.duplicated().sum())
print("Cleaned data saved to:", OUTPUT_PATH)
