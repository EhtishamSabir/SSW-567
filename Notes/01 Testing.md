# Lecture 01: Testing

## SDLC

Verficiation and testing is added to each stage of the Waterfall Model to improve system reliability
Rigorous testing must be completed before moving onto the next step
Testing is critical in any SDLC implementation

## Continuous Delivery

Similar to and frequently discussed with Agile Methods
Iterative but software is kept in a state where it is always ready for deployment
Does not have a seperate event of "software deployment" to prepare for release
Automation plays a key role in testing and development

## Testing

### Definition

**Testing**- a technical investigation of the system under test conducted to provide the stakeholders with quality-related information

Details of the definition of testing

- technical: technical means such as models, experimentation, mathematics, logic and tools
- investigation: an organized and thorough search for information. An active process with questions and analysis of results
- of the system under test: the complete system (software, hardware, data, documentation etc.) of everything delivered
- conducted to provide stakeholders: stakeholders are those with a vested interest in system success
- with quality-related information: often about faults and functionality. May include other information such as Process, Robustness, Reliability, Performance, Maintainability, etc.

### Forms of Testing

- Black Box: system is viewed as a "black box"
  - don't care about what happens in the system, just how the system interacts with its environment
- White Box: system is viewed as a "see-through box"
  - view interior of system logic to test internals
- System: test from perspective of system user (test system as a whole)
- Unit: test system unit-by-unit (unit can be a specific method, class etc.)
  - only care about how each unit works by itself
  - need both Unit and System testing (test that all units work and test that they work together)
- Acceptance: last form of testing before product is fully deployed
  - from point of view of customer
  - tests system in the environment and use cases that it will be deployed in

Test indivdual units -> test entire system -> test acceptance -> ship to customer
Verification: verifies that system and tests meet the requirements of the customer

### Dimensions to Classify Testing Models

- Life-Cycle Phase: requirements, architecture, design, unit, component, integration, system, acceptance (Alpha and Beta tests)
- Validation vs. Verification:
  - Verification: ensuring you got the correct product (deals with the intermediate steps such as documentation)
  - Validation: seeing if the product is 100% what you expected (deals with final product such as execution)
- Visibility into Internals: (Black vs. White vs. Grey Box)
- Function vs. Non-Functional:
  - Functional: scenario, feature
  - Non-Functional: performance, security, reliability, safety, stability
- Dynamic vs. Static:
  - Static: reviewing documentation, static code analysis but not actually executing code
  - Dynamic: how the system responds to dynamic tests
- Special Purpose: smoke, sanity, regression, GUI, interoperability, operational, usability

### Testing Terminology

- System Under Test (SUT): system to be tested
- faults: defects in the system that may or may not ever be seen in operation and cause failures
- failures: faults taht occur in operation
  - a fault **may** lead to a failure **but not always**
- errors: mistakes made by people
- defect metrics: measure faults
- reliability metrics: measure failures

### Faults vs. Failures

A program with buggy code that never executes:

- has many faults
- has no failures
- Mean Time Between Failures (MTBF) = infinity
- as it never fails, it is highly reliable

A program with only one bug that executes every time:

- has only one fault
- fails every time
- MTBF = 0
- always fails, it has low reliability

Failures can include

- application crashing
- unacceptable performance
- breaches in security
- loss of data
- missing functionality
- a design that prevents future enhancements
- unusable UX
- operationally unsupportable

### Testing to Find Faults

**Fault**: flaw that may cause a discrepancy between the expected result of an operation and the actual result
Faults can occur anywhere in the process (requirements, design, coding, configuration, data, etc.)
Software testing techniques are used to identify faults (differences between actual and expected)

### QA vs. Testing

Quality Assurance is the process for providing evidence to establish confidence among stakeholders

- process includes quality-related activities
- process monitoring and improvements
- meeting standards and procedures

QA is about assuring quality
Testing is what determines and measures quality

## Cost of Faults

Factors impacting cost of a fault

- when was it found?
  - how long after the change was committed?
    - found in unit testing -> low cost
    - specification problem found after releaase -> high cost
- how much throwaway work? how much rework?
- how much is schedule impacted?
- how critical will failures be?

### Fundamental Challenges in Testing

- why am I testing? (what is the testing mission?)
- how and what should I test? (what is the testing strategy?)
- how do I know whether a test passes or fails? (what is the oracle? critical for automation)
- when are we done? how much testing is enough? (can the system be completely tested?)
- how can I test quickly? (how to balance speed vs. thoroughness?)

### Testing Challenges

- What is the mission?
  - objective of testing is to provide quality related information to stakeholders. This information is relevant to their goals, objectives and needs (i.e. release readiness, certification, quality assessment, system feasibility, important bugs etc.)
- What is the strategy?
  - specify a plan to meet information needs of stakeholders
  - some items to consider:
    - what are we testing?
    - what kinds of tests must we use?
    - how many tests must be present?
    - how do we know when testing is adequate?
    - what features do we test?
    - under what conditions do we test?
- The Oracle
  - oracle has two parts
    - oracle information that represents expected output
    - oracle procedure that compares the oracle information with the actual output
- When are we done?
  - complete testing is possible on only the simplest systems
  - **System Release Criterion**: quality threshold which authorizes the project for release
  - testing can have diminishing returns for increased cost after a certain point
- Testing Fast Enough
  - need to balance speed and quality to remain competitive in the marketplace yet produce quality software
  - methods to test fast enough
    - **retrospection**: review development and test process
    - **test driven development**: test when the item is created
    - **continuous integration**: opimize process to identify problems early
