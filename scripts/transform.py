import pandas as pd
import re
import os

# Project root
project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Read dataset
input_file = os.path.join(
    project_root,
    "data",
    "raw",
    "combined_news.csv"
)

df = pd.read_csv(input_file)

print("Original Records:", len(df))

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove empty text records
df = df[df["text"].astype(str).str.strip() != ""]

# Remove null values
df.dropna(inplace=True)

print("Records After Cleaning:", len(df))

# Text cleaning function
def clean_text(text):
    text = str(text).lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()

# Clean news text
df["text"] = df["text"].apply(clean_text)

# Save cleaned data
output_file = os.path.join(
    project_root,
    "data",
    "processed",
    "clean_news.csv"
)

df.to_csv(output_file, index=False)

print("Clean dataset saved successfully!")
print("Saved at:", output_file)
print(df.tail())