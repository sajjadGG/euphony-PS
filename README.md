# Euphony with Property Signature

The Euphony with Property Signature system is designed to facilitate efficient program synthesis. This system guides the search strategy based on Probabilistic Higher Order Grammars (PHOGs) and augments it with property signatures derived from input-output example features. By combining these two methodologies, this system can incorporate input-output specification constraints, effectively narrowing down the search space while maintaining the ability to guide the search with the enumeration of likely programs.

## Overview

This system stems from the fundamental problem of program synthesis, where the goal is to find a program that satisfies high-level specifications given as input and output constraints. Given the enormity of the search space, heuristic functions guide the search, with learned heuristic functions tending to have repetitive patterns composed of reusable subprograms.

Our methodology combines three main concepts:

1. **Euphony**: An existing system that uses a learned probabilistic model (PHOG) to guide the search towards likely programs, assuming that desirable programs follow predictable patterns.
   
2. **PHOGs (Probabilistic Higher Order Grammar)**: A generalization of probabilistic context-free grammar, which for each production rule, allows conditioning beyond its parent node.
   
3. **Property Signatures**: A set of programs operating on given input-output pairs for a synthesis task, and their output used as features to narrow down the search for potential solution programs.

Our system extends the capabilities of Euphony by integrating property signatures to augment the production rule's context. 

## Results

On a small test set of string domain program synthesis tasks, we show that our method can increase search time efficiency, with significant performance gains across 15 out of 21 tasks.

## Future Work

Future work could investigate the effects of data diversity and dataset size on the efficacy of this method, and potentially look into augmenting the contexts used in PHOGs with alternatives to property signatures that still capture information from input-output specifications.

## Setup and Usage

Follow these instructions to run the program:

1. Copy `run_phog_learner` to `euphony/run_phog_learner.py`:
   ```
   cp run_phog_learner euphony/run_phog_learner.py
   ```
2. Navigate to the `euphony` directory:
   ```
   cd euphony
   ```
3. Follow the instructions detailed in the `README` file in the `euphony` directory.

4. Run the `run_phog_learner.py` script:
   ```
   python run_phog_learner.py
   ```
