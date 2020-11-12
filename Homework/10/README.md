# Homework 10: Performance Testing

**Author**: Liam Brew

**Date**: 11 November 2020

**Pledge**: I pledge my honor that I have abided by the Stevens Honor System

## Assignment Description

### Performance Testing

You are to do a performance test and analysis of a system of your choice, but the system must support multiple users.  I recommend that you use Apache JMeter for this assignment.  See below for instructions on getting started with JMeter.

### Step 1

Create a simple workload model for the system for a typical hour on a typical day. I expect to see a number of users with different scenarios that then become test cases. (Note: this does not have to be a totally realistic workload model.  I don't expect you to use real usage data.) What would you vary using user variables?

### Step 2

Try testing this with the performance testing tool. Document what you did and analyze the results of the test. Did you find anything interesting about the performance of this system?  

Your deliverable is a document that includes:

- a description of the system that you chose to test and the tool that you used to do performance testing
- a test plan
- the workload model that you tested including the scenarios tested
- screen dumps of the output from the tool on your test cases and test data
- performance graphs
- a discussion of your findings

## Testing Strategy

For this assignment, I will test Udemy.com through the use of JMeter. I decided upon this system as it is a popular website that contains many different sub-sections and catogories that must simulatanesouly support a large number of users from around the world. To replicate the conditions of a typical time on a typical day, I initially used five hundred threads/users to simulate what I expected to be realistic international traffic. These users were divided into three groups as explained below.

### Group 1: First Time Users

This group of users represents those who are new to Udemy and just discovered the website. I assigned 50% of the user base or 250 threads to this group. These users will first interact on the home page and then move on to the About Us page. I created this scenario as it represents users trying to learn more about what services Udemy.com has to offer. Since I assume that most visitors to the website do not have an account, I made this group the largest of the three and assigned it a ramp-up period of 125 seconds, resulting in a throughput of 2 users/second.

![Group 1](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/10/group1.png)

### Group 2: Business Users

This group represents those who have Udemy for Business accounts. These are different from regular accounts as they are provided by a person's employer to facilitate personal development and training. I decided to test this to see if there is a difference in backend infrastructure and/or resource allocation between the business and regular accounts. I was interested in seeing, for example, if Udemy perhaps valued a certain account more and therefore dedicated more resources to its operation. To account for the fact that not as many people have Udemy for Business accounts, I assigned this group 25% of the user base (or 125 threads) and gave it a ramp-up time of 125 seconds, resulting in a throughput of 1 user/second.

![Group 2](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/10/group2.png)

### Group 3: Software Testers

This group is the most niche and represents those looking for software testing courses. These users make use of the course search by first accessing the Development categories of courses. This lists all of the different software development fields that Udemy offers courses in, such as web design, testing, or shell scripting. Next, the user selects the Software Testing category to view this specific subset of courses. I assigned 25% of the user base to this group to represent those users actively searching for courses. To account for the relative niche status of this, I gave it a ramp-up time of 250 seconds to result in a throughput of .5 user/second.

![Group 3](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/10/group3.png)

### Workload Model Discussion

I believe that the Workload Model that most appropriately matches my testing plan is the Scenario Model. I believe that this is the case because testing plan targets specific features/locations over others. This has to do with the way I tried to classify users into their respective groups and assign stories and scenarios to each group. I tried to keep things varied enough to touch on all potential users and the most important functions of the website (first time visitors, users with a business account, users trying to log into their account (Group 2), users viewing the list of potential courses, and users looking for a specific course/subset of courses). Each of my tests are steeped in a specific scenario, hence my classification of this strategy is a Scenario Workload.

## Results

### Tabulated Results

![Results](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/10/results.png)

![Failure](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/10/failures.png)

![Summary Results](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/10/summary.png)

![Aggregate Results](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/10/aggregate.png)

### Graphed Results

![Graph Results](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/10/graph.png)

![Respone Times](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/10/response.png)

## Discussion of Results

I believe that this system for the most part passed my load testing. As you can see in my graphs, the performance and response times were relatively constant. While there were some deviations present occasionally, I do not believe that these were large enough to indicate a faulty system. One interesting anomaly that I did identify was the fact that all of the failures were caused by the About Us page. This leads me to believe that this page is a potential bottleneck in the performance of the system. Perhaps the developers assumed that not many people would access it at once? This can potentially be an issue if there is a sudden spike in new users on the website, such as what may happen after a successful update or product/press release. However, overall I will conclude that this website performed well.
