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

- Notebooks
  - `iteration_count.ipynb`
    - This notebook generates a text file called `pairs.txt` that specifies the number of iterations for each executable in a pair. The calculation is based on the constraint that both executables in a pair must be run for at least two iterations. The runtime information for each executable is obtained from the `runtime_individual.txt` file. If one executable has a shorter runtime, it will continue running until the paired executable completes its iterations. The contents of `pairs.txt` reflect the computed iteration counts for each executable pair.
  - `time trends.ipynb`
    - This notebook analyzes the runtimes of different executables using data from three files: `runtime_individual.txt`, `runtime_pairs.txt`, and `runtime_iterations.txt`. It generates bar plots for each executable, where the individual runtime is represented as a horizontal standard line. The runtime of each executable when paired with other executables is plotted as a ratio to the default time and displayed as bar charts.
    - All the generated plots are saved to a folder named "Plots" with the name of the corresponding executable.
 
 - `Project report` is detailed pdf report on project, one can refer to understanding mehtodology and details of board used for this analysis.
 - Check the What is Polybench pdf to know what exactly polybench processes are in breif
