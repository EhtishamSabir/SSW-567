# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

import math


def classifyTriangle(a, b, c):
    if (a <= 0 or b <= 0 or c <= 0) or (a > 200 or b > 200 or c > 200) or (a > (b + c)) or (b > (a + c)) or (c > (a + b)):
        return 'Not a valid triangle'

    if a == b and b == a and b == c:
        return 'Equilateral'
    elif (math.isclose((a ** 2) + (b ** 2), (c ** 2))):
        if(isScalene(a, b, c)):
            return 'Right and Scalene'
        if(isIsosceles(a, b, c)):
            return 'Right and Isosceles'
        return 'Right'
    elif(isScalene(a, b, c)):
        return 'Scalene'
    else:
        return 'Isosceles'


def isScalene(a, b, c):
    return (a != b) and (b != c) and (a != b)


def isIsosceles(a, b, c):
    return ((a == b) or (a == c) or (b == c))
