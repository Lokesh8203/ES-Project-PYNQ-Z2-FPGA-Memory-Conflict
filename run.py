import subprocess
import time

with open("exe.txt") as f:
    exes = f.read().splitlines()

for exe in exes:
    start = time.perf_counter()
    subprocess.run(f"./{exe}", shell=True)
    end = time.perf_counter()
    runtime = end - start
    with open("runtime_individual.txt", "a") as f:
        f.write(f"{exe} runtime: {runtime:.6f}s\n")
