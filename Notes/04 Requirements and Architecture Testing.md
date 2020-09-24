# Lecture 04: Requirements and Architecture Testing

## Requirements Testing

Test quality, correctness and completeness of customer requirements

Responsible for testing everything, not just the implementation

Possible questions (triangle assignments):

- what if the parameters describe an invalid triangle?
- what are the return values?
- what is the valid range of the values?

### Gathering Requirements

Goal: gather features and requirements for a new system

Compare and contrast three different approaches:

- Traditional Requirements: plan driven method requirements
  - gathering requirements is typically first step in a plan-driven SDLC
  - Business Analyst interviews the customer to extract features required from the system
  - describes all of the features needed by the customer
    - functional requirements (features)
    - non-functional requirements (availability)
  - Business Requirements Document (BRD): formal contract between the customer and the development team
- Use Cases: RUP approach for capturing requirements
  - describe different scenarios of how the user may use the system (users and actors)
  - specify all possible scenarios and expected flow, alternate, problem flows
  - typically include detailed instructions on how to accomplish those scenarios
- User Stories: agile approach for capturing requirements
  - customers communicate their needs via short statements
    - each statement describes the goal of an actor
  - customers provide the user stories with help from developers
  - each User Story is a reminder for the customer and developer to discuss the issue
  - customer should decide priority of each story

Properties of good requirements:

- unambiguous
- testable, measurable
- complete and correct

### Static Reviews

- Requirements Reviews and Inspections
  - extremely effective: defect removal efficiency of 60-70%
  - very structured and formal
  - QA should require reviews and inspections
  - test team should:
    - ensure reviews and inspections are done
    - participate in the process
    - review data to determine sections of requirements likely to change or contain errors
  - includes pair programming
  - why are inspections effective?
    - preparation: reviewers find issues that authors miss
    - peer pressure: forces authors to work more carefully
    - formal process: forces authors and reviewers to be thorough
    - focus: focus on highest payoff
- walkthroughs
  - similar to inspections but is more informal
  - serves as a forum to discuss alternatives and examine solutions
  - variable quality due to personalities
  - ad-hoc preparation
- peer reviews
  - can be inspection and/or walkthrough
- checklists
  - itemized list of all requirements to ensure that they are met
  - source code checklist
    - comments
    - poor style
    - bad smells
    - security threat model
    - code coverage
    - LINT issues

Requirements traceability

- forward traceability: ensure completeness of the specification, implementation and testing
- backward traceability: trace a product back to its source to verify that requirements remain current with design, code, and tests. defects are traced back to origin

Benefits of traceability

- trace every requirement from definition to test cases
- ensures that every requirement is implemented and tested (no missing and no extra)
- measure completeness of test coverage
- measure impact of a change request
- **Root Course Analysis**: where was the fault inserted?

Drawbacks of traceability

- requires a lot of effort
- can result in diminishing returns

### Dynamic Reviews

- prototypes
  - simplified model of a system but are effective for testing requirements
  - typically used in testing UX
    - hard to get right and requires many iterations
  - can prototype any part of a solution: UX, flows, interfaces, databases
    - recommended to havy many different prototypes of each system component
  - two types of prototypes
    - throwaway/rapid prototype: quick effort to test an idea; disposable
    - evolutionary prototype:
      - start with limited functionality
      - evolve over time to add features
      - prototype evolves into finished product
  - prototypes for testing (can be an Orcale): test
    - usability
    - requirements
    - design
    - test cases
  - advantages
    - engage customers early in SDLC
    - customer has better understanding of feature
    - explore many alternatives
    - identify missing or unneeded features
  - disadvantages
    - risk of over reliance on prototype and insufficient requirement analysis
    - customers may become confused between prototype and final system
    - prototype may lead to insufficient solution
- models
- verification and validation

## Architecture Reviews

Developed at Bell Labs to evaluate AT&T internal projects

**Architecture Review Board (ARB)**: value proposition to involve experts and detect problems early. Involves management, developers, customers, and QA

Principles

- need a clearly defined problem statement (focus of ARB)
  - drives system architecture
  - described by:
    - what system does
    - how it fits into the environment (system's form)
    - life-cycle cost and use of standard reusable parts
    - time (release dates)
    - operational in the desired environment
- product line and business application projects require a system architect at all phases (know requirements, constraints of entire system)
- independent experts conduct reviews
- reviews are open processes
- companies conduct reviews for the project's benefits

Intersection of technology, management and design

**Capability Maturity Model (CMM)**: methodology that measures, develops and refines an organization's software development process. Five levels:

1. initial: unpredictable and reactive
2. managed: managed on the project level
3. defined: proactive rather than reactive
4. quantitatively managed: measured and controlled
5. optimizing: stable, flexible, and continuous movement

Relevance of CMM to testing:

- software testing
- QA
- inspections
- architecture review boards
