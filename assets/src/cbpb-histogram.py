import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()

# Read csv
bloom = pd.read_csv("./assets/data/peak-bloom-clean.csv")
df = pd.DataFrame(bloom, columns = ['year', 'date', 'estimated_temp'])

# Compute number of data points
n_data = len(df)

# Number of bins is the square root of number of data points
n_bins = np.sqrt(n_data)

# Convert number of bins to integer
n_bins = int(n_bins)

# Convert str to date
df['date'] = df['date'].astype('str').str.zfill(4)
df['year_date'] = df['year'].astype(str) + df['date'].astype(str)
df['year_date'] = pd.to_datetime(df['year_date'])
df = df.sort_values('date')
date = df['year_date'].dt.strftime("%b %d")

def color_picker(shade, index):
    """Pick a color from cubehelix palette"""
    num_shades = shade
    color_list = sns.cubehelix_palette(num_shades)
    colors = color_list.as_hex()

    for color in colors:
        color = colors[index]
        return color

c = color_picker(30, 1)

# Draw the histogram
plt.hist(date, bins=n_bins, color=c)

# Label the axes
plt.xlabel('Cherry blossom peak-bloom date').set_color('#2d1e3e')
plt.ylabel('Number of flowering dates').set_color('#2d1e3e')
plt.xticks(rotation=70, color='#2d1e3e')
plt.yticks(color='#2d1e3e')

# Plot title
plt.title('Cherry blossom peak-bloom date in Kyoto, Japan (1678 - 2021)').set_color('#2d1e3e')

# Show the plot
plt.show()
