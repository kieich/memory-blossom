import matplotlib.pyplot as plt
import seaborn as sns
from numpy import arange

x = arange(36).reshape(6, 6)
cmap = sns.cubehelix_palette(dark=0, light=1, as_cmap=True)
ax = sns.heatmap(x, cmap=cmap, xticklabels=False, yticklabels=False, cbar=False)

plt.show()
