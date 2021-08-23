import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()

uniform_data = np.random.rand(10, 10)

cb_scale = sns.cubehelix_palette(as_cmap = True)
ax = sns.heatmap(uniform_data, cmap = cb_scale, vmin=0, vmax=1, xticklabels=False, yticklabels=False, cbar=False)

plt.show()
