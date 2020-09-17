# Docker and Configuration Management

I've worked with Docker on both school and industry projects before, so I fortunately have a bit of experience with containerization and the benefits that it brings. My answers to the following questions on Configuration Management are based on these experiences as well as the material from this week's lecture series, which I found to be very helpful and informative.

## Integration

A major problem frequently encountered in the integration phase of development is the sheer number of code sources and tools at play. Each of these sources can be viewed as an individual "moving part" that must be fit with all the others to ensure compatability and an operational system. Naturally, the more parts there are, the more difficult it is to fit them all together. One of the projects that I've worked on was very large and featured multiple programming languages, databases, and tools. I can confirm that managing the successful integration of all its components was a difficult task.

Docker helps alleviate integration issues by providing a level of standardization across the integration environments. This helps create, maintain, and disseminate a baseline working environment that is confirmed to be operational. As development proceeds and components are added or removed, any modifications that break this environment can be reverted using the image feature.

## Testing

A recurring issue with testing software is the presence of external errors that negatively impact the performance and results of tests. An example of this would be an improperly configured environment that causes otherwise perfect code to fail. This error may cause confusion and delays in the testing and therefore overall development process, as time must be spent ensuring each testing environment is up to development specifications. Additionally, in a worst-case scenario, an environment failure can decieve the team into believing the code is at fault, which causes only further hassle. I have a lot of experience with this, especially when working on library-intensive projects such as those featuring Maven and NodeJS.

Docker's standardization aspect is helpful in this as well. By posessing the afforementioned standardized working environment, it is very easy to set up test environments that guarantee the software will run on first try. Additionally, this ease of setting up test instances lends itself well to the portability of testing. Environments can easily be loaded onto a wide arrange of hosts, from physical machines to virtual machines to cloud resources, increasing the availability of testing for the project.

## Deployment

A common problem with deployment is creating the deployment environment itself. This environment needs to be comprehensive enough to support all the different components and functionality of a project, yet also minimalistic enough to reduce the size of the finalized product being shipped. Additionally, environments need to be tailored to work with the location on which they will be hosted. Conventionally, curating and maintaining a deployment environment has been an extensive task.

Docker's ease of configuration management enables the same environment used in development to be carried over into the deployment stage. Any changes necessary are easy to make and track as Docker operates very similarly to other version control systems.

## Customer Support

With an improper Configuration Management system, customer Change Requests can be an extensive and expensive process. Not only does the change to the code itself have to be created and tested, but this change must also be reflected in the environment on which it is hosted. A relatively simple software change, such as adding a new tool or updating the version of an existing one, can cause a large wmount of work in terms of modifying the environment.

Docker helps avoid this by facilitating the rapid deployment of environments. This lets development teams quickly ship updates and completed Change Requests to customers without having to spend additional time and resources on the deployment process itself. This allows required changes to be fit within the continuous deployment and testing cycle rather seamlessly. Additionally, in the case of errors and bugs, Docker's modular and compartmentalized nature makes it relatively easy to pinpoint where something went wrong.

## Security

Large projects that make use of many components are at an increased risk of security compromise. This is beacuse the more components there are, the more potential access points and backdoors that can compromise a system. Additionally, there exists the possibility of multiple components being secure unto themselves but may present vulnerabilities when combined with eachother. In a large project with a complex environment and configuration, it is difficult to detect security breaches and trace their location.

Docker improves the security of a project by dividing its workload amongst different containers, thereby protecting the inner processes of one container from another. Additionally, this has the benefit of reducing the coupling between different environments. If one environment is compromised, it can easily be separated from the rest, greatly reducing the likelihood of the breach spreading. It is easier to monitor multiple lean containers than a few larger and all-encompassing ones.
