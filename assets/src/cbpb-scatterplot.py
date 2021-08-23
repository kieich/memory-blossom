import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# Read csv
bloom = pd.read_csv("./assets/data/peak-bloom-clean.csv")
df = pd.DataFrame(bloom, columns = ['year', 'date', 'period', 'estimated_temp'])

# Convert str to date
df['date'] = df['date'].astype('str').str.zfill(4)
df['year_date'] = df['year'].astype(str) + df['date'].astype(str)
df['year_date'] = pd.to_datetime(df['year_date'])
df = df.sort_values('date')

# Generate a scatter plot
g = sns.relplot(x='date', y='year', data=df, kind='scatter', hue='estimated_temp', size='estimated_temp', alpha=0.7)

# Plot title
g.fig.suptitle('Cherry blossom peak-bloom date in Kyoto (1678 - 2021)', x=0.45, y=0.99, size='small')
g.set(xlabel='Peak-bloom date', ylabel="Year")

plt.xticks(rotation=70)

# Show plot
plt.show()
