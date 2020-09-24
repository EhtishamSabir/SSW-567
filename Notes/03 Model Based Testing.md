# Lecture 03: Model Based Testing

## Model

- simple representation of an artifact but preserves (at least approximates) important artifacts
- **Model-Based Testing (MBT)**: testing where the System Under Test (SUT) is compared to formal model created from the SUT's requirements
  - use a formal model of the SUT along with test generation tools to automatically generate relevant test cases
  - test case results from the SUT are compared agains the Model's expected results -> the Model becomes the Oracle

Advantages of MBT

- generating model improves understanding of SUT
- automate test case design & generation
  - may reduce cost
  - easier maintenance of regression tests
- more extensive testing possible
- more traceability

Disadvantages of MBT

- requires a formal model
  - effort moves from testing model to building the model
- models may be difficult to organize and develop
- models may be difficult to comprehend
- QA confidence depends on the accuracy of the model
- scaling may become an issue

Types of models

- structural
  - model of the structure of the system
  - what the system is
  - describes components, functionality and interactions
- behavioral mdoels
  - model the behaviour of the system
  - what the system does not how it does it
  - needed for testing

Strategies for model building

- form representation of the system's functionality
  - understand system behaviour before modeling
  - understand inputs, outputs, and actions to build a model
- description needs to be written down in an easily understandable form and should be as formal as possible
  - useful models make test generation easier and automatable
  - many formal modeling techniques to describe behaviors
- large, complex systems may require the team to use formal modeling techniques

Model coverage

- some percentage of a model that is included in a testing suite for some coverage criteria
- testing suite is a collection of test cases
- coverage criteria is what is used to control the test-generation process

## Decision Tables

|Inputs|Values|1|2|3|
|------|------|-|-|-|
|Input 1|Y,N|Y|Y|Y|
|Input 2|Y,N|Y|N|N|
|Input 3|Y,N|N|N|N|
|Effects||||
|Effect 1||x|x||
|Effect 2||||x|

Lists causes (inputs and values) and effects (results) in a table

Each column represents a unique combination of inputs: table helps to structure logic in a verifiable form

Steps:

1. combine mutually exclusive inputs
2. calculate total combinations
3. list all input value combinations
4. reduce combinations
5. check covered combainations

**Checksum**: each column represents a number of combinations. Calculate the sum of all combinations and compare it with step 2

Why use decision tables

- easy to observe that all possible conditions are accounted
- make you consider all combinations of inputs and outputs
- improved specification and test case visibility
- able to generate code from decision tables

## State Machines

FSM: Finite State Machines

- composed of states and transitions
  - every transition contains an input event and next state
  - transition can also define outputs and actions
  - FSM operations by taversing from state to state

State table: every FSM state transition diagram has a corresponding state table

Test cases from the state diagram/table

- the state table does not include cases that have no clear cut action or result
- test cases specify every possible outcome of state and command

Test primitives can be used that test every individual test transition

**GraphWalker** open source tool using FSMs to drive test generation

Model coverage for FSM

- all-states: for each state of the model there is a test case that contains the state
- all-transitions: for each transition of the model there is a test case that contains the transition
- all-events: the same for every event that is used in any transition
- all-paths: all possible transition sequences have to be included in the test suite

## Markov Chains

FSM with probabilities for each transition. E.g., probability that the next state is Sj given that the current state is Si

Still need to test all combinations, but probabilities provide more clues for load, stress and reliability testing as well as in simulations

### UML State Charts/State Charts

Extend FSMs to be hierarchical to model large systems as a set of subsystems. However, FSMs can become unwieldy quickly

Grammars are a way of formally specifying the structure of languages

- used to describe inputs to a system and to also generate test data
- use cases
  - language-based apps (compilers, interpreters)
  - protocol-based implementations
  - can be used to model behaviors of systems

Disadvantages of state charts

- model may be difficult to understand
- behavior of complex system model may not be transparent
- negative cases may be implicit but not defined
