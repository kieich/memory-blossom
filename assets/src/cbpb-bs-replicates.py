import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()

# Read csv (1946 - 1995, outlier=1990)
bloom = pd.read_csv("./assets/data/peak-bloom-short2.csv")
df = pd.DataFrame(bloom, columns = ['year', 'date', 'estimated_temp'])
bloom_date = df['date']

def color_picker(shade, index):
    """Pick a color from cubehelix palette"""
    num_shades = shade
    color_list = sns.cubehelix_palette(num_shades)
    colors = color_list.as_hex()

    for color in colors:
        color = colors[index]
        return color

c = color_picker(30, 1)

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points
    n = len(data)

    # x-data for the ECDF
    x = np.sort(data)

    # y-data for the ECDF
    y = np.arange(1, len(x)+1) / n

    return x, y

def bootstrap_replicate_1d(data, func):
    """Generate bootstrap replicate of 1D data."""
    bs_sample = np.random.choice(data, len(data))
    return func(bs_sample)

bs_replicates = np.empty(10000)

def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""

    # Initialize array of replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)

    return bs_replicates

# Take 10,000 bootstrap replicates of the mean
bs_replicates = draw_bs_reps(bloom_date, np.mean, 10000)

# Compute and print SEM (Standard error of the mean)
sem = np.std(bloom_date) / np.sqrt(len(bloom_date))
print('sem:', sem)

# Compute and print standard deviation of bootstrap replicates
bs_std = np.std(bs_replicates)
print('std:', bs_std)

# Bootstrap confidence interval
conf_int = np.percentile(bs_replicates, [2.5, 97.5])

# Print the confidence interval
print('95% confidence interval =', conf_int)

# Make a histogram of the results
plt.hist(bs_replicates, bins=50, density=True, color=c)
plt.xlabel(r'$\tau$ (dates)').set_color('#2d1e3e')
plt.ylabel('PDF').set_color('#2d1e3e')
plt.xticks(color='#2d1e3e')
plt.yticks(color='#2d1e3e')

# Plot title
plt.title('Cherry blossom peak-bloom date in Kyoto, Japan (1946 - 1995)').set_color('#2d1e3e')

# Show the plot
plt.show()
