# Lecture 02: Configuration Management

## Overview

Software Configuration Management (SCM) challenges:

- projects include components from many sources
  - source code, libraries, documentation, hardware etc.
- each component may have dependencies
- components change as well as their dependencies
- confounded and complicated by many versions

Some artifacts include:

- source code
- dependent libraries
- API version dependencies
- dev tools
- requirements
- defects
- test cases
- testing tools
- releases and versions

SCM questions:

- do we have the correct version of each component?
- how do we track the contents of each release?
- which run time environment (cloud, server, device etc.)?
- what happens on version change?
- is the QA environment the same as production?

Symptoms of inadequate SCM:

- changes get lost
- time wasted fixing wrong version of a feature
- bugs reappear
- integration problems
- missed and incorrect tests

SCM beyond deployment and test:

- SCM improves productivity and quality
- helps detect accidental and intentional changes

**Configuration Management (CM)**: tools and processes that control and manage the artifacts and configurations of a system

- Information Technology Infrastructure Library (ITIL): set of practices for IT that focuses on aligning IT services with business needs
- Configuration Management Database (CMDB): keeps release records of all configuration items

## 3,4,5 of Software Configuration Management

3 objectives of SCM:

- repeatability: can we repeat the same steps twice (build, test, configure, deploy)?
- traceability: can we know exactly what we went into creating what was delivered?
- integrity: can we be certain that we have included exactly what we intended and nothing else?

SCM provides control during development (productivity, traceability, preventing insider attacks) and operations (system integrity and repeatability to scale)

Potential issue with SCM: control can become the objective rather than mission success

4 SCM concepts:

- baslines: specific version of an artifact that has been formally agreed upon. Once baselined, the item becomes a configuration item and can only be changed through the change control process
- configuration item (CI): lowest unit of the items being managed and controlled
  - configuration items can be grouped and aggregated to form hierarchies
- versions, variants and releases
  - version: an instance of a CI that is functionally distinct from other CI instances
    - versions beyond the original baseline have a derivation history that describes the previous versions
      - maintains a record of changes made
  - variant: an instance of a system that is functionally identical but non-functionally distinct from other instances
  - release: an instance of a system which is distributed to users outside the development team
- change control: requirement that changes must not be haphazard
  - changes made before the baseline can be quick and easy, but after should follow the change control process
  - enforce change control to minimize risk

### 5 SCM processes

### (1) Change Management

- track change requests
- decide whether to a make a change or not
  - **Change Request (CR)**: a requested change to a system
    - capture the following attributes **on creation**:
      - change request ID
      - what is the change?
      - why is it proposed?
      - who proposed it?
      - when is the change needed?
      - what are the risks of making the change?
    - add attributes as the process proceeds:
      - evaluation of the change: impact analysis, project costs
      - dispostion: approved, rejected, deferred, under investigation
    - evaluation: informal cost benefit analysis. What is needed, why, and what's the impact? CR triage is evaluating the severity and priority of a change request
      - **Change Control Review Board (CCRB)**: evaluates change requests. Membership depends upon the project and typically includes members from all SDLC stages

### (2) Configuration Identification

- process to identify the attributes of every aspect of a CI
- CIs are documented and baselined
- purpose
  - ensure correct versions of all components
  - enable recreating the CI with exactly the same components
  - have a baseline to prevent tampering
- challengs:
  - large number of CIs and IDs
  - single CR may impact many CIs
  - each platform may require different variants
- techniques
  - use version numbers to maintain unique versions of a CI
  - use attribute-based identification to associate a version with attributes (date, creator, language, customer etc.)
  - use change-oriented identification to maintain chain sets for easy tracking (system based)
- **Application Release Naming Scheme: X.Y.Z**
  - X: major version. Large upgrades; not backwards-compatible
  - Y: minor version. Upgrades and bugfixes; backwards-compatible
  - Z: patch version. Bug fixes; backwards-compatible
- distributed version control system: allows collaboration (GitHub)

### (3) Software Builds

- different methods: deferred integration (Waterfall) vs. continuous integration (Agile)
- continuous integration best practices
  - maintain single source code repository
  - automate testing and build process
  - build and test in deployment environment
  - frequent commits to ensure up-to-date testing
- continuous integration benefits
  - reduced risk
  - detect and fix bugs more quickly and easily
  - fewer bugs associated with automated testing
  - enables continuous delivery to customers

### (4) Release Management

- process to ensure upgrades/features/fixes are delivered to meet project and customer needs
- frequency of new feature releases
  - slow: operating systems, mission critical systems
  - fast: web-based services, Spotify, Amazon, Netflix
- traditional, periodic releases
  - major release/upgrade: major new features and enhancements. 6-12 month intervals
  - minor release (Point Release): enhancements and bug fixes. 1-2 month intervals
  - emergency fixes/patches: high priority feature and fixes that can't wait until the next minor release. Deployed as needed
- new releases are more than just software and include configuration files for each distinct installation, data files used in system operation, installation scripts, documentation, packaging, and marketing
- release issues
  - development issues
    - too many releases may cause churn and cost
    - releases not tested sufficiently causing customer issues
    - late releases
  - customer/support issues
    - minimize number of supported releases
    - customer may not want an upgrade
    - customers may skip intermediate releases, increasing support costs
- Agile methods increase speed of delivery
  - Agile release train: multiple Agile teams delivering functionality. Time boxed iterations with quality requirements. Features in each release may change to meet schedule, and deliveries are made every time the train "enters the station"
  - DevOps: source control/configuration management. Build tools automate the build process every time a change is committed to source control. All testing must be automated, e.g. TDD. This includes unit, integration, system, performance, security, and acceptance testing
- **feature toggles**: hide incomplete features to users
- continuous deployment: continuous...
  - development
  - testing
  - integration
  - delivery
  - monitoring

### (5) Auditing and Status Accounting

- auditing
  - mechanism to determine how closely the current state of a system matches its baseline
  - important for security, maintenance, and support
- status accounting
  - mechanism to maintain a record of how a system has evolved
  - maintain a record of the state of the system relative to published documents and agreements

## Containers

- consider roles for the following:
  - dev/test
    - implement and test new features
    - identify, fix, and test bugs
  - operations
    - deploy
    - monitor
    - customer support
- dev/test CM issues
  - dev/test must work on the "right" version of the code and right depends on context. They must build against the right version of all tools and libraries
    - patching a high priority bug for current release?
    - fixing a bug for upcoming release?
    - building new features for upcoming release?
- what can go wrong?
  - dev/test
    - wasted time
    - "lost" fizes
    - differences between Dev and Ops
    - differences between developers
  - operations
    - wasted time
    - customer unhappy
    - missed business opportunities
    - excessive costs
    - security threats
- benefits of Docker
  - separate app components into standalone and self-contained modules
  - each container has all code, libraries, and utilities needed to run
  - develop, debug, test, and deploy in the same environment
  - each container is isolated to improve security. This enables modular container management in the case of issues
