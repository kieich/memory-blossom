import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()

# Read csv (1946 - 1995, outlier=1990)
bloom = pd.read_csv("./assets/data/peak-bloom-short2.csv")
df = pd.DataFrame(bloom, columns = ['year', 'date', 'estimated_temp'])

bloom_date = df['date']
temp = df['estimated_temp']

def color_picker(shade, index):
    """Pick a color from cubehelix palette"""
    num_shades = shade
    color_list = sns.cubehelix_palette(num_shades)
    colors = color_list.as_hex()

    for color in colors:
        color = colors[index]
        return color

c = color_picker(20, 18)
line = color_picker(20, 5)

# Plot the peak bloom date versus estimated temperature
plt.plot(bloom_date, temp, marker='.', linestyle='none', color=c)
plt.margins(0.02)
plt.xlabel('peak bloom date')
plt.ylabel('estimated_temp')

# Perform a linear regression
a, b = np.polyfit(bloom_date, temp, 1)

# Print the results to the screen
print('slope =', a, 'estimated temp / peak bloom date')
print('intercept =', b, 'estimated temp')

# Make theoretical line to plot
x = np.array([400, 430])
y = a * x + b

# Add regression line to the plot
plt.plot(x, y, color=line)

# Label the axes
plt.xlabel('Cherry blossom peak-bloom date').set_color('#2d1e3e')
plt.ylabel('Estimated temperature').set_color('#2d1e3e')
plt.xticks(color='#2d1e3e')
plt.yticks(color='#2d1e3e')

# Plot title
plt.title('Cherry blossom peak-bloom date + temp. in Kyoto, Japan (1946 - 1995)').set_color('#2d1e3e')

# Draw the plot
plt.show()
