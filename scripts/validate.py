import pandas as pd
import os

# Project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read combined dataset
file_path = os.path.join(
    project_root,
    "data",
    "raw",
    "combined_news.csv"
)

df = pd.read_csv(file_path)

# Validation checks
total_records = len(df)
null_values = df.isnull().sum()
duplicate_records = df.duplicated().sum()

empty_text = 0
if "text" in df.columns:
    empty_text = (df["text"].astype(str).str.strip() == "").sum()

# Print results
print("===== DATA VALIDATION REPORT =====")
print("Total Records:", total_records)
print("Duplicate Records:", duplicate_records)
print("Empty Text Records:", empty_text)

print("\nMissing Values:")
print(null_values)

# Save report
report_path = os.path.join(
    project_root,
    "reports",
    "data_quality_report.txt"
)

with open(report_path, "w") as f:
    f.write("===== DATA VALIDATION REPORT =====\n\n")
    f.write(f"Total Records: {total_records}\n")
    f.write(f"Duplicate Records: {duplicate_records}\n")
    f.write(f"Empty Text Records: {empty_text}\n\n")

    f.write("Missing Values:\n")
    f.write(str(null_values))

print("\nReport saved successfully!")