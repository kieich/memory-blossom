import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# Read csv
bloom = pd.read_csv("./assets/data/peak-bloom-clean.csv")

df = pd.DataFrame(bloom, columns = ['year', 'date', 'period', 'estimated_temp', 'ratio'])

# Convert str to date
df['date'] = df['date'].astype('str').str.zfill(4)
df['year_date'] = df['year'].astype(str) + df['date'].astype(str)
df['year_date'] = pd.to_datetime(df['year_date'])
df = df.sort_values('date')

# Divide date(ratio) into quartiles
df['date_quartile'] = pd.qcut(df['ratio'], q = 4, labels = False)

# Set a color palette
color_palette = sns.cubehelix_palette(reverse=True, as_cmap=True)

# Create scatter plot
sns.scatterplot(x=df['year_date'].dt.strftime("%b %d"), y='year', hue='date_quartile', data=df, palette=color_palette, legend=False, size='estimated_temp', alpha=.9)

# Label the axes
plt.xlabel('Cherry blossom peak-bloom date')
plt.ylabel('Year')
plt.xticks(rotation=70)

# Plot title
plt.title('Cherry blossom peak-bloom date in Kyoto, Japan (1678 - 2021)')

# Show the plot
plt.show()
