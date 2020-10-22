# Homework 07: Scenario Testing

**Author**: Liam Brew

**Date**: 20 October 2020

**Pledge**: I pledge my honor that I have abided by the Stevens Honor System

## Assignment Description

You were recently hired by company to do system testing of one of their brand new products. The product is a programmable door lock. The product can be used to secure any doors that it fits, but the company is specifically targeting this product to be used to to secure classroom doors in schools.

Deliverables:

1. Create and describe three scenario tests.
2. Create and describe one soap opera scenario test.
3. Create and describe three negative tests.

## Summary of Work

In this assignment I created a number of different tests to study the operation of a Haifuan door lock. These tests included scenario tests to test specific end-to-end runthroughs of device usage, a soap opera scenario test to test extenuating circumstances which have many different impacts on the system, and negative tests to determine the system's efficiency in dealing with suboptimal effects.

## Scenario Tests

The scenario tests that I've created are as follow:

1. Test Device Initialization
  
    - see if the RST button is pressed for 6 seconds
    - test if the system is initialized
      - see if factory state is restored
      - see if admin code is now "123456"

    This test serves to run through the process by which a user sets up and initializes their machine. It should be the first test conducted to ensure that the system is operational.

2. Set User Code

    - see if "*" and "#" are pressed simultaneously
    - see if the correct admin code is entered followed by "#"
      - test if the user properly authenticates and validates said code
    - see if "2" is pressed
    - see if a user code is entered followed by "#"
      - test if the system saves this code and registers it as a valid one to gain access

    This test represents a more complicated one than the initial test has it has to do with saving and recognizing user input as well as data.

3. Set Remote Control (applicable only for remote cotnrol version)

   - see if "*" and "#" are pressed simultaneously
   - see if the correct admin code is entered followed by "#"
      - test if the user properly authenticates and validates said code
   - see if "2" is pressed
   - see if the system detects the pressing of the controller's unlocked button
   - see if the system recognizes this button as being the unlock button
   - see if the system registers this controller as valid.

   This tests represents an even more complex one than previously. It requires interaction with a remote controller, reading and interpreting signals, and saving/updating data.

## Soap Opera Scenario Test

Gregg bought a Haifuan lock for the lab. He set it up on the door for the lab and set an admin code and user code. For ease of use, he also set the Haifuan lock to work with a card, remote control and fingerprint. Eventually one day Gregg forgets his user code. He realized that he gave his card to someone else, the remote control is out of batteries, and that the touch sensor is dirty enough wherein it won't read his fingerprint. The cleaning liquid for the sensor is locked in the lab. Since he is the only one with access, he figures it would be easiest to just delete all users instead of trying to guess his code or retrieve one of the materials. He enters the admin code, which he remembered, deletes all users, and re-adds himself once into the lab.

This soap opera scenario tests the following features of the system:

- initalization (Gregg setting up and installing the Haifuan lock)
- setting user code (Gregg setting his inital user code)
- setting card (Gregg setting his card)
- setting remote control (Gregg registering the remote)
- setting fingerprint (Gregg registering his finger print)
- enter system control (Gregg enters the admin code to navigate to system commands)
- delete all users (Gregg deletes all users)

## Negative Tests

The negative tests that I've created are as follow:

1. Damaged ID Card

    - user attempts to use a damaged ID card that is unreadable by the system

    This test represents a scenario that is likely to happen over the course of the system's use. The system should deny this authentication request.

2. Unverified Remote Control

    - user attempts to use a standard IR device (such as those found on certain Android phones) to interact with the system.

    This test represents a potential threat scenario in which the system may be taken advantage of. The system should deny this authentication request.

3. Loss of Power

    - the power is purposefully cut to the system to see how it reacts

    This test represents an extenuating circumstance which the system should be prepared to operate in. Here, system priorities need to be determined, such as either favoring safety (unlocking the system in this state) or security (locking it).

## Challenges

A notable challenge that I encountered while completing this assignment was that I did not directly work on the technical side of the product being tested. Normally, when I am writing tests I am technically familiar with the inner workings and behaviours of the system. This was not the case here, as I had to rely on someone else's technical specifications. I can see how this relates to what dedicated QA testers must go through in the real world.

## Reflection

This assignment was interesting as it focused on conceptual ideas that have an impact on testing. As mentioned in the **Challenges** section, I felt that it was a good way to replicate existing real-world scenarios of testing projects. By developing tests with no exposure to the technical workings of a system, I believe that this helps the development process itself. Now, I can better plan and account for projects before technical development work on them has begun.
