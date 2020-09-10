import math

def classify_triangle(a, b, c):
    if(not is_valid_triangle(a, b, c)):
        return("Not a valid triangle")
    elif((a == b) and (a == c) and (b == c)):
        return "Equilateral"
    elif ((a == b) or (a == c) or (b == c)):
        if(is_right_triangle(a, b, c)):
            return "Isosceles and Right"
        return "Isosceles"
    else:
        if(is_right_triangle(a, b, c)):
            return "Scalene and Right"
        return "Scalene"

def is_right_triangle(a, b, c):
    if(round(a**2, 0) + round(b**2, 0) == round(c**2, 0)):
        return True
    return False

def is_valid_triangle(a, b, c):
    if((a + b > c) and (a + c > b) and (b + c > a)):
        return True
    return False

if __name__ == "__main__":
    print(classify_triangle(1, 2, 3))

    print(classify_triangle(2, 2, 2))

    print(classify_triangle(2, 2, 3))

    print(classify_triangle(1, 1, math.sqrt(2)))

    print(classify_triangle(3, 4, 6))

    print(classify_triangle(3, 4, 5))


    