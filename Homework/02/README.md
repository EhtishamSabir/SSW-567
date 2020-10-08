# SSW567 Homework 05

Pipeline Status: [![build status of master](https://travis-ci.org/Liam-Brew/SSW-567.svg?branch=master)](https://travis-ci.org/Liam-Brew/SSW-567)

**Author**: Liam Brew

**Date**: 07 October 2020

**Pledge**: I pledge my honor that I have abided by the Stevens Honor System

## Assignment Description

The objective of this assignment is to apply the techniques from the lecture to static testing of your Triangles program. Specifically:

You will run a static code analyzer on your code, e.g. Pylint, identify and fix any problems reported by the static code analyzer;
You will run a code coverage tool on your code, e.g. Coverage.py, and extend your test cases to demonstrate at least 80% code coverage;
In this assignment, you will need to download and install the tools that you will need for static code analysis and code coverage.  You will then run those tools locally on your laptop to get the results.

Any changes that you make to your programs should be pushed up to GitHub.

## Summary of Work

I found this assignment to be interesting. While I had linting tool previously installed, it was not as in-depth as Pylint itself. I found Pylint to be very useful in detecting syntax errors and making code look good. Likewise, I found Coverage.py to be very useful as well. I am pleased to report that my initial coverage for the triangle.py tests was 95%, and this value only increased after I brought triangle.py up to static analysis specifications.

## Output

### Initial Static Analysis

![Initial Static Analysis](..\..\src\Homework\02\initial_lint.png)

### Final Static Analysis

![Final Static Analysis](..\..\src\Homework\02\initial_lint.png)

### Initial Coverage Analysis

![Initial Coverage Analysis](..\..\src\Homework\02\initial_coverage.png)

### Final Coverage Analysis

![Final Coverage Analysis](..\..\src\Homework\02\final_coverage.png)

### HTML Coverage Report

~Please disregard my virual environment's contribution to these metrics~

![HTML Coverage Report](..\..\src\Homework\02\coverage_html.png)

## Challenges

The most difficult challenge I encountered was dealing with some of the more precise Pylint issues. I found these to be frustrating yet at the same time relatively to implement. I did not encounter any issues with Coverage.py due to my test cases already being in object-oriented format.

## Reflection

I enjoyed this assignment and felt that it served to familiarize me with new tools that will increase the quality of my code. I will definitely look into using these more in the future, especially the potential automation of them.
