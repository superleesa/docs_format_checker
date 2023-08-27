import numpy as np
from math import sqrt
from random import randint, shuffle

def create_middle_and_pale_color(color_in_hex):
    """

    (white - givenColor)/2 + givenColor

    creates a middle color for the given color
    :param color_in_hex:
    :return:
    """

    color_in_rgb = np.array(hex_to_rgb(color_in_hex))
    white = np.array([255, 255, 255])

    middle_color = ((white - color_in_rgb) / 3 + color_in_rgb).round()
    pale_color = ((white - color_in_rgb)*2 / 3 + color_in_rgb).round()

    return rgb_to_hex(middle_color), rgb_to_hex(pale_color)

# print(create_middle_color([188, 235, 233]))

def hex_to_rgb(color_in_hex):
    """

    :param color_in_hex: it is assumed that red, green, blue take exactly two digits
    :return:
    """

    red = color_in_hex[1:3]
    green = color_in_hex[3: 5]
    blue = color_in_hex[5: 7]

    return int(red, base=16), int(green, base=16), int(blue, base=16)

def rgb_to_hex(color_in_rgb):
    return "#" + hex(int(color_in_rgb[0]))[2:] + hex(int(color_in_rgb[1]))[2:] + hex(int(color_in_rgb[2]))[2:]

def generate_random_color():
    DISTANCE = 5373

    min_first_axis = get_smaller_value_of_quadratic_equation(1, -510, 65025-DISTANCE)
    first_axis_value = randint(min_first_axis, 255)

    min_second_axis = get_smaller_value_of_quadratic_equation(1, -510, 65025+first_axis_value-DISTANCE)
    second_axis_value = randint(min_second_axis, 255)

    third_axis_value = get_smaller_value_of_quadratic_equation(1, -510, 65025+first_axis_value+second_axis_value-DISTANCE)

    list_of_axes = [first_axis_value, second_axis_value, third_axis_value]
    shuffle(list_of_axes)  # mutates list_of_axes

    # convert rgb to hex
    return rgb_to_hex(list_of_axes)


def get_smaller_value_of_quadratic_equation(a, b, c):
    numerator = -b - sqrt(b**2 - 4*a*c)
    denominator = 2*a

    return round(numerator / denominator)