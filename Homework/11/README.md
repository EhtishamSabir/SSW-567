# Homework 11: Testing Progress

**Author**: Liam Brew

**Date**: 18 November 2020

**Pledge**: I pledge my honor that I have abided by the Stevens Honor System

## Assignment Description

You are responsible for system testing of a new release.  You have 8 weeks total, and you're already at the end of week 6.  You need to pull together a presentation for your boss on release status, and whether you think it will be ready to go at the end of 8 weeks.

Here's the type of data you have:

-system testing status: # planned, executed, and passed
-operational profile testing status: failures per week (normalized to have same usage rate as expected in the field)
-defect status: total open, new defects discovered that week, closed that week
-historical data for last few releases

Your ship criteria is:

- system reliability of <= 2 failures per day in operation

Your testing completion criteria is:

- \>= 99% tests executed
- \>=98% tests passed
- <= 20 open defects

Use the specified data to create and submit a report for management that describes the status of testing and answers the following questions:

- will the release be ready to ship in 2 weeks? Why or why not?
- given the historical data about previous releases, how many defects do you expect to find one year after the code is released?

## Summary

In order to determine the status of the system test progress at the end of the deadline, I graphed the thus-far accumulated data in a series of charts and tables. From this, I was able to extrapolate the data to estimate the project's status for the final two weeks. I was therefore able to determine that the system is on schedule and barring any major unexpected delays will be ready to ship in the next two weeks, satisfying all of the criteria to ship and complete testing.

## Determination of Acceptability

### System Testing Status

To determine the status of the system testing at the end of the development lifecycle, I examined the historical data of the testing plan. This was provided from week one through week six and contained the amount of tests planned, executed, and passed each week. I estimated the data for the remaining weeks through the use of Excel's linear forecast feature on the historical data. For week seven I found the number of executed tests to be 375, with the number passing to be 305 (rounded down). For week eight I found the number of executed tests to also be 375, with all passing. This data was the same at the end of week eight which represented its state at the end of development. As both the number of tests executed and passed were higher than 99%, this indicates a **successful testing plan completion**. The table below displays the testing status for each week, with the following chart offering a visible interpretation of this data.

| Week | Planned | Executed | Passed     |
|------|---------|----------|------------|
| 1    | 25      | 18       | 12         |
| 2    | 50      | 76       | 19         |
| 3    | 100     | 102      | 75         |
| 4    | 200     | 175      | 100        |
| 5    | 325     | 270      | 200        |
| 6    | 375     | 350      | 280        |
| 7    | 375     | 375      | 305        |
| 8 (Start)| 375 | 375      | 375        |
| 8 (End)  | 375 | 375      | 375        |

![Testing Status](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/11/tests.png)

### FI/FO Analysis

To determine the expected reliability of the system at the end of the final week of development, I examined the system's historical failure intensity. This data was provided starting at week three through to week six. I extrapolated this data to create an estimate of the reliability for the remaining two weeks. I performed this extrapolation by first determining the underlying equation for FI through Excel's trendline feature. I found the FI formula to be ```FI = 746.6 * ((Week #)^(-3.096))```. This formula allowed me to obtain FI values for the remaining two weeks, which I determined to be 1.81 and 1.19 for weeks seven and eight respectively. From here I found the FI/FIO ratio for the remaining two weeks, which was .905 and .595. At the end of week eight, which would signify an end to the development period, I found the project's FI value to be .83 and it's FI/FIO ratio to be .415. Under the provided criteria this value is acceptable, which indicates that the **system is reliable enough to ship**. The table below displays the total FI and FI/FIO values for the project, with the following chart offering a visible interpretation of this data.

| Week     |     FI            |     FI/FIO        |
|----------|-------------------|-------------------|
|     3    |     25            |     12.5          |
|     4    |     12            |     6             |
|     5    |     6             |     3             |
|     6    |     3             |     1.5           |
|     7    |     1.81          |     0.905         |
| 8 (Start)|     1.19          |     0.595         |
| 8 (End)  |     0.83          |     0.415         |

![FI/FIO Ratio Over Development Life](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/11/fio.png)

### Defect Status

The historical data for defects included backlog, new and closed counts for each week starting at the first week and ending at the sixth. Plotting these, the following relationship is examined:

![Historical Tracking](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/11/defects.png)

To predict the remaining week's defect data, I utilized the Rayleigh Defect Model. This is because when compared to the Exponential and S-Curve Models, the Rayleigh Model gives insight into the entire development lifecycle and not just the testing and deployment processes. Using Excel's mathematical formulas, I determined the mean K values for New and Closed Defects to be 289.2 and 272.7 respectively. For the standard deviation K values for New and Closed Defects, I determined the values to be 88.7 and 110.2 respectively. Using these calculated values, I was able to determine the remaining week's defect values, which are seen in the table below.

| Week  | Backlog | New  | Closed |
|-------|---------|------|--------|
| 1     | 0       | 10   | 5      |
| 2     | 5       | 40   | 20     |
| 3     | 25      | 30   | 40     |
| 4     | 15      | 50   | 50     |
| 5     | 15      | 60   | 50     |
| 6     | 25      | 30   | 50     |
| 7     | 5       | 28   | 26     |
| 8 (Start)| 7    | 20   | 19     |
| 8 (End)  | 8    | 13   | 13     |

Note that these values are rounded up. I figured that it would be better this way as this would indicate a "worst-case scenario" of more defects than anticipated. I rounded as to me it did not seem possible to have a percentage of a defect. By the end of week eight, eight defects will be carried over. This is a result of the formula ```(Backlog + New) - Closed```. **This value falls within the accepted criteria, making the system eligible for release**. Adding these new values to the previous relationship chart illustrates the finalized defect graphing as seen below:

![Final Tracking](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/11/final_defects.png)

## Conclusion

I determined that the system will be ready for release by the end of the development cycle. Using the extrapolation of historical data, I predicted that all criteria of a successful release will be met. The system has been tested thoroughly, with >= 99% of planned tests executed and >= 98% of those passing. The system reliability is in order, and there will be less than eight defects open at the time of release. Therefore I predict this release to be successful.
