def next_color(col: str)->str:
    """Takes a light color and returns the next one in a row.
    "red"->"orange"->"green"

    Examples:
        >>> next_color("red")
        'orange'
        >>> next_color("green")
        'red'
        >>> next_color("orange")
        'green'
    """
    if col=="red":
        return "orange"
    elif col=="orange":
        return "green"
    else:
        return "red"

# print(next_color("red") =="orange")
# print(next_color("green") == "red")
# print(next_color("orange") == "green")
# print(next_color("black"))

import doctest
doctest.testmod(verbose=True) # verbose=True for more details