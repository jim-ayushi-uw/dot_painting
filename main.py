import colorgram
rgb_colors = []
colors = colorgram.extract('imagee.jpg', 25)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)


#the output list after extracting the colors from image
color_list = [(213, 157, 89), (238, 214, 95), (34, 106, 151), (126, 168, 198), (152, 76, 54), (208, 134, 163), (211, 85, 62), (155, 61, 82), (22, 39, 54), (173, 161, 49), (200, 87, 121), (136, 183, 151), (57, 117, 91), (228, 168, 187), (240, 212, 5), (27, 47, 38), (88, 156, 99), (66, 47, 34), (38, 165, 188), (227, 175, 166), (10, 98, 75)]
