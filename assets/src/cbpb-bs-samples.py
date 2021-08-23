import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()

# Read csv (1946 - 1995, outlier=1990)
bloom = pd.read_csv("./assets/data/peak-bloom-short2.csv")
df = pd.DataFrame(bloom, columns = ['year', 'date', 'estimated_temp'])

def color_picker(shade, index):
    """Pick a color from cubehelix palette"""
    num_shades = shade
    color_list = sns.cubehelix_palette(num_shades)
    colors = color_list.as_hex()

    for color in colors:
        color = colors[index]
        return color

c = color_picker(20, 18)
dot = color_picker(20, 8)

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points
    n = len(data)

    # x-data for the ECDF
    x = np.sort(data)

    # y-data for the ECDF
    y = np.arange(1, len(x)+1) / n

    return x, y

# Size of the resampled array
print('Size:', len(df['date']))

for _ in range(50):
    # Generate bootstrap sample
    bs_sample = np.random.choice(df['date'], size=len(df['date']))

    # Compute and plot ECDF from bootstrap sample
    x, y = ecdf(bs_sample)
    plt.plot(x, y, marker='.', linestyle='none', color=dot, alpha=0.1)

mean = np.mean(bs_sample)
print('mean:', mean)

median = np.median(bs_sample)
print('median:', median)

std = np.std(bs_sample)
print('std:', std)

# Compute and plot ECDF from original data
x, y = ecdf(df['date'])
plt.plot(x, y, marker='.', color=c)

# Make margins and label axes
plt.margins(0.02)
plt.xlabel('Cherry blossom peak-bloom date').set_color('#2d1e3e')
plt.ylabel('ECDF').set_color('#2d1e3e')
plt.xticks(color='#2d1e3e')
plt.yticks(color='#2d1e3e')

# Plot title
plt.title('Cherry blossom peak-bloom date in Kyoto, Japan (1946 - 1995)').set_color('#2d1e3e')

# Show the plot
plt.show()
