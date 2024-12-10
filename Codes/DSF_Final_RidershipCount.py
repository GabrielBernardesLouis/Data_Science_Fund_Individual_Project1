import pandas as pd
import matplotlib.pyplot as plt

# Load the newly uploaded dataset for subway entries
#file_path_entries = '/mnt/data/MBTA_Gated_Station_Entries.csv'
file_path_entries = '/Users/gabriel/Downloads/MBTA_Gated_Station_Entries.csv'
entries_data = pd.read_csv(file_path_entries)

# Display the first few rows and structure of the dataset
entries_data.head(), entries_data.info()

# Convert service_date to datetime and extract the month-year for aggregation
entries_data["service_date"] = pd.to_datetime(entries_data["service_date"])
entries_data["month_year"] = entries_data["service_date"].dt.to_period("M")

# Aggregate total gated entries by month-year
monthly_entries = entries_data.groupby("month_year")["gated_entries"].sum()

# Create a visualization of total entries per month
plt.figure(figsize=(14, 7))
monthly_entries.plot(kind="bar", color="skyblue", edgecolor="black")

# Enhance the plot
plt.title("Total Subway Entries per Month", fontsize=16)
plt.xlabel("Month-Year", fontsize=12)
plt.ylabel("Total Gated Entries", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

# Display the plot
plt.show()
