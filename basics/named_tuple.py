"""
A lightweight tuple with more readability

example: (10,50,100) - tuple that represents RGB color code
in-order to access value of a color, we need to access using indexes - what if new developer doesn't know
what this tuple represents

- Named tuple can be used here for more readability
"""

from collections import namedtuple

colors = (10, 50, 100)
print(colors[1])

# we can use dict for holding these values

colors_dict = {'red': 10, 'green': 50, 'blue': 100}
print(colors_dict['green'])  # gives same result

# but we choosen the tuple - maybe we need immutability & with dict, we need to type in key's everytime

# define named tuple once

Color = namedtuple('Color', ['red', 'green', 'blue'])
colors_tuple = Color(green=10, red=50, blue=100)
colors_tuple2 = Color(10, 50, 100)
print(colors_tuple.green)
print(colors_tuple2.green)

