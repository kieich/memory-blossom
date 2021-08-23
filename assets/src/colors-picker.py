import seaborn as sns
sns.set()

def color_picker(shade):
    """Pick a color from cubehelix palette"""
    num_shades = shade
    # color_list = sns.cubehelix_palette(num_shades)
    color_list = sns.color_palette("autumn_r", 10)
    colors = color_list.as_hex()

    return colors

colors = color_picker(12)
print(colors)
