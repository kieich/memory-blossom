import seaborn as sns
sns.set()

def color_picker(shade, index):
    """Pick a color from cubehelix palette"""
    num_shades = shade
    color_list = sns.cubehelix_palette(num_shades)
    colors = color_list.as_hex()

    for color in colors:
        color = colors[index]
        return color

c = color_picker(20, 3)
print(c)
