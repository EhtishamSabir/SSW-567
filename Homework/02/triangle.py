"""Determines if a set of three input values form a triangle,
and if so classifies the type of triangle."""
import math

def classify_triangle(side_a, side_b, side_c):
    """Determines if a series of values form a triangle,
    and if so classifies said triangle."""

    return_str = ""

    non_zero = (side_a <= 0 or side_b <= 0 or side_c <= 0)
    sides_compared = side_comparison(side_a, side_b, side_c)
    over_max = is_over_max(side_a, side_b, side_c)

    if non_zero or over_max or sides_compared:
        return_str += 'Not a valid triangle'
    elif side_a == side_b and side_b == side_a and side_b == side_c:
        return_str += 'Equilateral'
    elif math.isclose((side_a ** 2) + (side_b ** 2), (side_c ** 2)):
        if is_scalene(side_a, side_b, side_c):
            return_str += 'Right and Scalene'
        elif is_isosceles(side_a, side_b, side_c):
            return_str += 'Right and Isosceles'
        else:
            return_str += 'Right'
    elif is_scalene(side_a, side_b, side_c):
        return_str += 'Scalene'
    else:
        return_str += 'Isosceles'
    return return_str

def is_over_max(side_a, side_b, side_c):
    """Determines if any side is above the max (200)."""
    return (side_a > 200) or (side_b > 200) or (side_c > 200)

def side_comparison(side_a, side_b, side_c):
    """Determines if one side is greater than the other two combined."""
    a_greater = (side_a > (side_b + side_c))
    b_greater = (side_b > (side_a + side_c))
    c_greater = (side_c > (side_a + side_b))
    return a_greater or b_greater or c_greater

def is_scalene(side_a, side_b, side_c):
    """Determines if a triangle is scalene."""
    return (side_a != side_b) and (side_b != side_c) and (side_a != side_c)

def is_isosceles(side_a, side_b, side_c):
    """Determines if a triangle is isosceles."""
    return (side_a == side_b) or (side_a == side_c) or (side_b == side_c)
