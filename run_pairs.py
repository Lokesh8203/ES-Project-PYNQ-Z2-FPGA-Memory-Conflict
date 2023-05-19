import subprocess
import threading
import time

# define executables
exes = ['2mm', '3mm', 'adi', 'atax', 'bicg', 'correlation', 'covariance',
        'deriche', 'doitgen', 'durbin', 'fdtd-2d', 'floyd-warshall',
        'gemm', 'gemver', 'gesummv', 'gramschmidt', 'heat-3d', 'jacobi-1d',
        'lu', 'ludcmp', 'mvt', 'nussinov', 'symm', 'syr2k', 'syrk', 'trisolv',
        'trmm']

# Define a function to run an executable for a given number of times and calculate the average runtime
def run_exe(exe_name):
    start_time = time.time()  # Record the start time
    subprocess.run([f"./{exe_name}"])
    end_time = time.time()  # Record the end time
    total_time = end_time - start_time  # Calculate the total time taken
    return total_time

# Define a function to run an executable in a separate thread
def run_exe_thread(exe_name, results):
    runtime = run_exe(exe_name)
    results.append((exe_name, runtime))

# define function to run an executable and save its runtime to a file
def run_exe_pairs(exe):
    print(f"Running {exe} in pairs")
    runtime_file = open("runtime_pairs.txt", "a")
    
    results = []
    t1 = threading.Thread(target=run_exe_thread, args=(exe, results))
    t2 = threading.Thread(target=run_exe_thread, args=(exe, results))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    runtime = results[0][1]
    runtime_file.write(f"Runtime for {exe}: {runtime:.4f} seconds\n")
    runtime_file.close()
         
for exe in exes:
    run_exe_pairs(exe)

