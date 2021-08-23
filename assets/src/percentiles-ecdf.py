import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# Read csv
bloom = pd.read_csv("./assets/data/peak-bloom-clean.csv")

df = pd.DataFrame(bloom, columns = ['year', 'date', 'period', 'estimated_temp'])

# Specify array of percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles
ptiles_date = np.round(np.percentile(df['date'], percentiles))
print('percentiles:', ptiles_date, ptiles_date.dtype)

# Convert percentiles from float to date
ptiles_date = ["19870%.0f" % i for i in ptiles_date]
ptiles_date = pd.to_datetime(ptiles_date)
ptiles_date = ptiles_date.strftime("%m%d")

# Convert str to date
df['date'] = df['date'].astype('str').str.zfill(4)
df['year_date'] = df['year'].astype(str) + df['date'].astype(str)
df['year_date'] = pd.to_datetime(df['year_date'])
df = df.sort_values('date')

# Comparing percentiles to ECDF
# x-data for the ECDF
x = np.sort(df['year_date'].dt.strftime("%m%d"))

# y-data for the ECDF
y = np.arange(1, len(x)+1) / len(x)

def color_picker(shade, index):
    """Pick a color from cubehelix palette"""
    num_shades = shade
    color_list = sns.cubehelix_palette(num_shades)
    colors = color_list.as_hex()

    for color in colors:
        color = colors[index]
        return color

c = color_picker(20, 3)
dot = color_picker(20, 18)

# Generate plot
plt.plot(x, y, marker='.', linestyle='none', color=c)

# Overlay percentiles as pink hexagon
plt.plot(ptiles_date, percentiles/100, marker='h', markersize=5, linewidth=1, color=dot, linestyle='none')

# Label the axes
plt.xlabel('Cherry blossom peak-bloom date').set_color('#2d1e3e')
plt.ylabel('ECDF').set_color('#2d1e3e')
plt.xticks(rotation=60, color='#2d1e3e')
plt.yticks(color='#2d1e3e')

# Keeps data off plot edges
plt.margins(0.02)

# Plot title
plt.title('Cherry blossom peak-bloom date in Kyoto, Japan (1678 - 2021)').set_color('#2d1e3e')

# Show the plot
plt.show()
