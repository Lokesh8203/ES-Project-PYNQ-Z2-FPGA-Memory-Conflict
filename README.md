## ES3305 - Mini Project Spring 2023
# Memory contention analysis for co-executing workloads
# Guide - Dr. Rajesh Kedia

This repository contains the pyhton scripts, notebooks and output runtime text files for analyzing the memory contention on polybench processes.

- Polybench
  - [Polybench is a collection of kernels and solvers for a variety of numerical algorithms that are widely
used in scientific computing.](https://github.com/Meinersbur/polybench/tree/master/polybench-code)
  - The `exe.txt` file in repository includes the names of polybench process executables in a sequences, used as input for scripts.

- Run scripts and runtime files
  - Individual run
    - `run_individual.py` script runs each executable once and appends runtime of each of them to `runtime_individual.txt`
  - Pairwise run
    - `run_pairs.py` script runs each executable in two instances at same time and then save runtime of the first instance to `runtime_pairs.txt`
  - Iteration run
    - In this scenario, multiple instances of different executables are run simultaneously. Each executable is paired with another executable, and the constraint is that when a pair of executables is being run, both executables must be run for at least two iterations. The executable with the shorter runtime will continue running until the iterations of the paired executable are completed. Only after both executables have finished their iterations, the pair is considered completed, and the average runtime of both executables over the number of iterations is saved.
    - `run_iteratoins` is script which will run the pair of executables and append their runtimes to `runtime_iterations.txt`
    - 
 
