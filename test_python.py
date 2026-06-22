import pandas as pd

fake = pd.read_csv('data/raw/Fake.csv')
true = pd.read_csv('data/raw/True.csv')

print("fake records:",len(fake))
print("true records:",len(true))