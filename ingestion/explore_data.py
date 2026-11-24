
import pandas as pd
from pathlib import Path
import io
import contextlib

# Define data location
DATA_PATH = Path("data/raw")

# Load dataset
events = pd.read_csv(DATA_PATH / "events.csv")

# Capture output
output = io.StringIO()

with contextlib.redirect_stdout(output):

    print("\n========== DATASET OVERVIEW ==========")

    print("\nDataset shape:")
    print(events.shape)

    print("\nFirst 5 records:")
    print(events.head())

    print("\nColumn information:")
    events.info()

    print("\nMissing values:")
    print(events.isnull().sum())

    print("\nDuplicate records:")
    print(events.duplicated().sum())

    print("\nEvent types:")
    print(events["event"].value_counts())

    print("\nUnique visitors:")
    print(events["visitorid"].nunique())

    print("\nUnique products:")
    print(events["itemid"].nunique())

    print("\nTimestamp range:")
    print(
        pd.to_datetime(events["timestamp"], unit="ms")
        .agg(["min", "max"])
    )

# Display results in terminal
print(output.getvalue())

# Save results to text file
with open("data/dataset_exploration.txt", "w", encoding="utf-8") as f:
    f.write(output.getvalue())

print("\nExploration results saved successfully!")



# Additional data quality checks

print("\n========== DATA QUALITY CHECKS ==========")

print("\nDuplicate rows:")
print(events[events.duplicated()].head(10))

print("\nTransaction ID availability by event:")
print(events.groupby("event")["transactionid"].apply(
    lambda x: x.notna().sum()
))

print("\nUnique transaction IDs:")
print(events["transactionid"].nunique())

print("\nEvents per visitor (summary):")
print(events.groupby("visitorid").size().describe())
