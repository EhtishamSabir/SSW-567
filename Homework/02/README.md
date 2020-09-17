# Homework 02: Legacy Classify Triangle Testing

**Author**: Liam Brew

**Date**: 16 September 2020

**Pledge**: I pledge my honor that I have abided by the Stevens Honor System

## Assignment Description

Sometimes you will be given a program that someone else has written, and you will be asked to fix, update and enhance that program. In this assignment you will start with an existing implementation of the classify triangle program that will be given to you. You will also be given a starter test program that tests the classify triangle program, but those tests are not complete.

In order to determine if the program is correctly implemented, you will need to update the set of test cases in the test program. You will need to update the test program until you feel that your tests adequately test all of the conditions. Then you should run the complete set of tests against the original triangle program to see how correct the triangle program is. Capture and then report on those results in a formal test report described below. For this first part you should not make any changes to the classify triangle program. You should only change the test program.

Based on the results of your initial tests, you will then update the classify triangle program to fix all defects. Continue to run the test cases as you fix defects until all of the defects have been fixed. Run one final execution of the test program and capture and then report on those results in a formal test report described below.

## Summary

I found the initial tests to be lacking in scope and complexity. They did not test for all of the potential outcomes of the program, and the tests that were there were insufficient. I believed them to be too similar to be valid. In response, I added two tests for every type of triangle and two for invalid triangles. To improve the thoroughness of my tests I included non-integer values in some of them.

### Reflection

As a result of this assignment I was able to appreciate the difficulty in testing another person's code. Because I was not familiar with the code when I wrote the tests for it, I found myself being extra thorough to make up for this. While this is better for the project, both writing the tests and modifying the code to pass them took longer than if I just wrote the code and tests myself.

### Results Metrics

|                | Test Run 1 (Initial)                                            | Test Run 2                                                                                                                                | Test Run 3                                                                                                                                                                      | Test Run 4 (Improved)                                                                                                                                                                                                                                                                                   |
| -------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tests Planned  | testRightTriangleA testRightTriangbleB testEquilateralTriangleA | testEquilateralTriangleB testIsoscelesTriangleA testIsoscelesTriangleB testScaleneTriangleA testScaleneTriangleB                          | testValidTriangleA testValidTriangleB                                                                                                                                           | testRightAndIsoscelesTriangleA testRightAndIsoscelesTriangleB testRightAndScaleneTriangleA testRightAndScaleneTriangleB                                                                                                                                                                                 |
| Tests Executed | testRightTriangleA testRightTriangbleB testEquilateralTriangleA | testEquilateralTriangleA testEquilateralTriangleB testIsoscelesTriangleA testIsoscelesTriangleB testScaleneTriangleA testScaleneTriangleB | testValidTriangleA testValidTriangleB testEquilateralTriangleA testEquilateralTriangleB testIsoscelesTriangleA testIsoscelesTriangleB testScaleneTriangleA testScaleneTriangleB | testRightAndIsoscelesTriangleA testRightAndIsoscelesTriangleB testRightAndScaleneTriangleA testRightAndScaleneTriangleB testValidTriangleA testValidTriangleB testEquilateralTriangleA testEquilateralTriangleB testIsoscelesTriangleA testIsoscelesTriangleB testScaleneTriangleA testScaleneTriangleB |
| Tests Passed   | 0                                                               | 0                                                                                                                                         | 2                                                                                                                                                                               | 12                                                                                                                                                                                                                                                                                                      |
| Defects Found  | if a <= 0 or b < = b or c <= 0:                                 | if a == b and b == a                                                                                                                      | elif ((a^2) + (b^2)) == (c \* 2) if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b))                                                                                          | elif a^2 + b^2 == c^2 or a^2 + cv2 == b^2 or c^2 + b^2 == a^2 elif (a != b) and (b != c) and (a != c) if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int))                                                                                                                             |
| Defects Fixed  | if a <= 0 or b < = b or c <= 0:                                 | if a == b and b == a                                                                                                                      | elif ((a^2) + (b^2)) == (c^2) if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b))                                                                                             | elif a^2 + b^2 == c^2 or a^2 + c^2 == b^2 or c^2 + b^2 == a^2 elif (a != b) and (b != c) and (a != c) if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int))                                                                                                                             |

## Initial classifyTriangle() Test Results

| Test ID                        | Input                 | Expected Results       | Actual Result | Pass or Fail |
| ------------------------------ | --------------------- | ---------------------- | ------------- | ------------ |
| testValidTriangleA             | 0, 0, 0               | 'Not a valid triangle' | InvalidInput  | Fail         |
| testValidTriangleB             | 0, 1, 2               | 'Not a valid triangle' | InvalidInput  | Fail         |
| testEquilateralTriangleA       | 1, 1, 1               | 'Equilateral'          | InvalidInput  | Fail         |
| testEquilateralTriangleB       | 1.1, 1.10, 1.10       | 'Equilateral'          | InvalidInput  | Fail         |
| testIsoscelesTriangleA         | 2, 2, 3               | 'Isosceles'            | InvalidInput  | Fail         |
| testIsoscelesTriangleB         | 3.1, 3.1, 5.12        | 'Isosceles'            | InvalidInput  | Fail         |
| testScaleneTriangleB           | 6, 7, 8               | 'Scalene'              | InvalidInput  | Fail         |
| testScaleneTriangleA           | 6.8, 7.3, 8.01        | 'Scalene'              | InvalidInput  | Fail         |
| testRightAndIsoscelesTriangleA | 1, 1, math.sqrt(2)    | 'Right and Isosceles'  | InvalidInput  | Fail         |
| testRightAndIsoscelesTriangleB | 7, 7, 7\*math.sqrt(2) | 'Right and Isosceles'  | InvalidInput  | Fail         |
| testRightAndScaleneTriangleA   | 3, 4, 5               | 'Right and Scalene'    | InvalidInput  | Fail         |
| testRightAndScaleneTriangleB   | 15, 20, 25            | 'Right and Scalene'    | InvalidInput  | Fail         |

## Improved classifyTriangle() Test Results

### Shell Output

```sh
Microsoft Windows [Version 10.0.18363.1082]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\liamb\OneDrive\Documents\Coursework\SSW 567>C:/Users/liamb/AppData/Local/Programs/Python/Python38-32/python.exe "c:/Users/liamb/OneDrive/Documents/Coursework/SSW 567/Homework/02/TestTriangle.py"
Running unit tests
............
----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```

### Test Report

| Test ID                        | Input                 | Expected Results       | Actual Result          | Pass or Fail |
| ------------------------------ | --------------------- | ---------------------- | ---------------------- | ------------ |
| testValidTriangleA             | 0, 0, 0               | 'Not a valid triangle' | 'Not a valid triangle' | Pass         |
| testValidTriangleB             | 0, 1, 2               | 'Not a valid triangle' | 'Not a valid triangle' | Pass         |
| testEquilateralTriangleA       | 1, 1, 1               | 'Equilateral'          | 'Equilateral'          | Pass         |
| testEquilateralTriangleB       | 1.1, 1.10, 1.10       | 'Equilateral'          | 'Equilateral'          | Pass         |
| testIsoscelesTriangleA         | 2, 2, 3               | 'Isosceles'            | 'Isosceles'            | Pass         |
| testIsoscelesTriangleB         | 3.1, 3.1, 5.12        | 'Isosceles'            | 'Isosceles'            | Pass         |
| testScaleneTriangleB           | 6, 7, 8               | 'Scalene'              | 'Scalene'              | Pass         |
| testScaleneTriangleA           | 6.8, 7.3, 8.01        | 'Scalene'              | 'Scalene'              | Pass         |
| testRightAndIsoscelesTriangleA | 1, 1, math.sqrt(2)    | 'Right and Isosceles'  | 'Right and Isosceles'  | Pass         |
| testRightAndIsoscelesTriangleB | 7, 7, 7\*math.sqrt(2) | 'Right and Isosceles'  | 'Right and Isosceles'  | Pass         |
| testRightAndScaleneTriangleA   | 3, 4, 5               | 'Right and Scalene'    | 'Right and Scalene'    | Pass         |
| testRightAndScaleneTriangleB   | 15, 20, 25            | 'Right and Scalene'    | 'Right and Scalene'    | Pass         |

### Assumptions and Inputs

I modified the provided code to work with non-integer values. From my studies in geometry, I felt that constraining triangles to be integer-only is insufficient. To accomplish this I used an approximation in the Pythagorean calculator to replicate real-world conditions (in the real world, a (1,1,sqrt(2)) triangle is considered Right).

### Tools

I made use of the Math library to provide square root functionality, which I used in the inputs of some of the test cases.
