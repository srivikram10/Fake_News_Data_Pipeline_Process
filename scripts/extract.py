import pandas as pd
import os

# project root and path of the datasets
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

fake_path = os.path.join(project_root, "data", "raw", "Fake.csv")
true_path = os.path.join(project_root, "data", "raw", "True.csv")

print("Fake Path:", fake_path)
print("True Path:", true_path)

# Read datasets
fake = pd.read_csv(fake_path)
true = pd.read_csv(true_path)

print("Fake rows:", len(fake))
print("True rows:", len(true))

# Add labels
fake["label"] = 0    # Fake News
true["label"] = 1    # Real News

# Merge datasets
df = pd.concat([fake, true], ignore_index=True)

# Shuffle data
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save combined dataset
combined_path = os.path.join(
    project_root,
    "data",
    "raw",
    "combined_news.csv"
)

df.to_csv(combined_path, index=False)

print("Dataset merged successfully!")
print("Saved at:", combined_path)
print("Total Records:", len(df))

print(df.tail())


