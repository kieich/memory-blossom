import pandas as pd
import matplotlib.pyplot as plt

# Read csv
bloom = pd.read_csv("./assets/data/peak-bloom-clean.csv")

df = pd.DataFrame(bloom, columns = ['year', 'date', 'period', 'estimated_temp', 'ratio'])

# Convert str to date
df['date'] = df['date'].astype('str').str.zfill(4)
df['year_date'] = df['year'].astype(str) + df['date'].astype(str)
df['year_date'] = pd.to_datetime(df['year_date'])
df = df.sort_values('year')

# Divide data into quartiles
df['date_decile'] = pd.qcut(df['ratio'], q = 10, labels = False)

# Export CSV for D3.js practice
df.to_csv(r'/Users/kieichikawa/Downloads/df-quartile.csv')

print(df)
