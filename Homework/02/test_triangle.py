"""Performs unit testing on triangle classification found in triangle.py."""

from classify_triangle import classify_triangle
import unittest
import math
import sys

class TestTriangles(unittest.TestCase):
    def testValidTriangleA(self):
        self.assertEqual(classify_triangle(0, 0, 0),
                         'Not a valid triangle', '0,0,0 is not a triangle')

    def testValidTriangleB(self):
        self.assertEqual(classify_triangle(0, 1, 2),
                         'Not a valid triangle', '0, 1, 2 is not a triangle')

    def testEquilateralTriangleA(self):
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classify_triangle(1.1, 1.10, 1.100),
                         'Equilateral', '1.1,1.10,1.10 should be equilateral')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classify_triangle(2, 2, 3),
                         'Isosceles', '2,2,3 should be isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classify_triangle(3.1, 3.1, 5.12),
                         'Isosceles', '3.1,3.1,5.12 should be isosceles')

    def testScaleneTriangleA(self):
        self.assertEqual(classify_triangle(6, 7, 8),
                         'Scalene', '6,7,8 should be scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classify_triangle(6.8, 7.3, 8.01),
                         'Scalene', '6.8,7.3,8.01 should be scalene')

    def testRightAndIsoscelesTriangleA(self):
        self.assertEqual(classify_triangle(1, 1, math.sqrt(
            2)), 'Right and Isosceles', '1,1,2^.5 is a Right and Isosceles triangle')

    def testRightAndIsoscelesTriangleB(self):
        self.assertEqual(classify_triangle(7, 7, 7*math.sqrt(2)),
                         'Right and Isosceles', '7,7,7*(2^.5) is a Right and Isosceles triangle')

    def testRightAndScaleneTriangleA(self):
        self.assertEqual(classify_triangle(
            3, 4, 5), 'Right and Scalene', '3,4,5 is a Right and Scalene triangle')

    def testRightAndScaleneTriangleB(self):
        self.assertEqual(classify_triangle(
            15, 20, 25), 'Right and Scalene', '15,20,25 is a Right and Scalene triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
