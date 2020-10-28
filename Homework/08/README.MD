# Homework 08: Usability Testing

**Author**: Liam Brew

**Date**: 28 October 2020

**Pledge**: I pledge my honor that I have abided by the Stevens Honor System

## Assignment Description

Part 1 - conduct a usability test to evaluate the usability of a website.  

Specifically, you should:

1. Create a test plan

    - What are you going to test, e.g. which website?
    - How are you going to test?
    - How will you measure the the results?
    - Recruit at least 1 test subject
    - You'll need to give the subject time to participate in the testing so start early on this assignment
    - Ask your subject to perform at least one Direct Task and at least one Scenario Task - make sure that your subject is not familiar with the site, so choosing a - popular site such as amazon or ebay may make it more difficult to find a subject

2. Collect relevant measures
    - Time to complete the tasks, number of errors, etc
    - Ask your subjects to complete John Brooke's System Usability Scale

Part 2 - test the accessibility of the site

For this part you will use one or more of the tools listed on the WC3 Web Accessibility Initiative site to test and evaluate accessibility.  Specifically, you should:

- Select one (or more tools) from the list of tools outlined [here](https://www.w3.org/WAI/ER/tools/?q=wcag-20-w3c-web-content-accessibility-guidelines-20)
- Use it to evaluate and assess the web site for accessibility.

There are 100+ tools to choose from. I will make no recommendations on which to use, and I will leave that up to you. I suggest that you poke around and try a few out to see what they do and how they work before finalizing on any one.

## Summary of Work

In this assignment I recruited a family member to help me analyze the usability and accessibility of a website. To determine if a website is sufficiently user-friendly, I gauged the experience of my subject in navigating it and performing different tasks, such as Direct and Scenario tasks. Some metrics that I observed include the average time it took them to complete a task, the number of errors and mistakes they made, and the score they assigned the website via John Brooke's System Usability Scale.

## Part 1 Deliverables

### Experimental Method

I decided to examine a very popular and well-loved website for this assignment: [mySteven's self services](https://mystevens.stevens.edu/sso/webselfservices.php). I chose this as Stevens faculty and students unfortunately need to interact with it very frequently. To complete the task, I had my test subject perform two tasks: one Direct task, which was to view the current transcript, and one Scenario task, which featured them looking for the information of a course being offered next semester. Throughout the course of the experiment I asked questions pertaining to the user interface of the website and the experience my subject dealt with.

### Test Subject

I had my father serve as a test subject for this experiment. I chose him because he is not very technologically experienced besides interaction with common websites (Facebook, Google, Amazon etc.). myStevens represents a more obscure website that I know for certain he has never interacted with before. I let him use my account to access the site and run through the tests. While he never used myStevens before and is not skilled at technology, he did attend college, so he was familiar with the terminology in play such as transcripts, terms, schedules et cetra.

### Quantitative Data

During the testing, I collected the following quantitative data:

- Time: 7 minutes and 7 seconds
- User Errors (2):
  - Initially used the 'Course Sections' feature to perform course data lookup instead of the 'Course Section Search' feature
  - Failed to select term prior to viewing the 'Course Section Search' feature
- System Errors (2):
  - Random session timeouts occur to frequently to be a security 'feature'
  - Term is oftentimes not remembered once selected

### System Usability Scale

At the end of the run-through, I had my subject complete John Brooke's System Usability Scale. The results of this are shown below:

![Brooke Usability Results](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/08/brooke_usability.png)

Using the scale's score calculation formula, I determined my subject's usability score to be: 2.6 * 22 = **55**, thereby giving this website a below average rating.

### Observations

I observed my subject frequently being unsure of what dropdown menu to select from the navigation bar at the top of the screen. They were often times unsure of where to find certain features due to the confusing naming scheme of the different headers (e.g., they initially thought the 'Course Section Search' feature would be found under the 'Registration' tab). Other than that, I found my subject to be capable of performing their tasks. They did point out that the styling of the website was antiquated and their user impressions were pretty lacking.

### Part 1 Summary

I found this experiment to be good practice in understand the point of view of the user when designing UX features. It reminded me a lot of the storyboarding that my team and I completed for our Engineering Design VI project. I feel that I will incorporate usability testing in the future while working on projects as it did give me significant insight into how the average, non-technical user tends to interact with things.

## Part 2 Deliverables

### Tool Selection

I decided to use the Google Developer Lighthouse for this portion of the assignment. This tool generates various reports that indicate a website's quality, including categories such as Performance, Best Practice Usage, Accessibility and SEO. Additionally, this tool allows users to report on both the Mobile and Desktop view of a website. I chose this tool as it is integrated in the Chrome Developer Console, which I am already familiar with.

### Accessibility Test Results

The results of the Google Developer Lighthouse's Acessibility Report are found below:

![Accessibility Results](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/08/accessibility.png)

As you can see, this score can be considered as sub-sufficient.

### Part 2 Summary

I did not encounter any issues or difficulties for this component of the assignment. I observed that accessibility testing tools are powerful items to use in testing the quality of a site, as I did not even consider to look for items such as proper ```aria``` usage. I found this assignment to be useful in ensuring proper compliance to accessibility guidelines to create a usable website for all.
