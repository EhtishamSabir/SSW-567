import unittest
import triangle as tri
import math 

class TestTriangle(unittest.TestCase):
    
    def test_invalid(self):
        self.assertEqual(tri.classify_triangle(1, 2, 3), "Not a valid triangle", "1,2,3 is not a triangle")
        
    def test_equilateral(self):
        self.assertEqual(tri.classify_triangle(2, 2, 2), "Equilateral", "2,2,2 is equilateral")

    def test_isosceles(self):
        self.assertEqual(tri.classify_triangle(2, 2, 3), "Isosceles", "2,2,3 is isosceles")
        
    def test_isosceles_right(self):
        self.assertEqual(tri.classify_triangle(1, 1, math.sqrt(2)), "Isosceles and Right", "2,2,3 is isosceles and right")

    def test_scalene(self):
        self.assertEqual(tri.classify_triangle(3, 4, 6), "Scalene", "3,4,6 is scalene")

    def test_scalene_right(self):
        self.assertEqual(tri.classify_triangle(3, 4, 5), "Scalene and Right", "3,4,5 is scalene and right")

if __name__ == "__main__":
    unittest.main()
