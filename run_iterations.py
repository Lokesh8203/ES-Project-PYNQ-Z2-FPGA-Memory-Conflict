import subprocess
import threading
import time

# Define a function to run an executable for a given number of times and calculate the average runtime
def run_exe(exe_name, num_runs):
    start_time = time.time()  # Record the start time
    for i in range(num_runs):
        print(f"Running {exe_name} for the {i+1} time")
        subprocess.run([exe_name])
    end_time = time.time()  # Record the end time
    total_time = end_time - start_time  # Calculate the total time taken
    avg_time = total_time / num_runs  # Calculate the average time per run
    return avg_time

# Define a function to run an executable in a separate thread
def run_exe_thread(exe_name, num_runs, results):
    avg_runtime = run_exe(exe_name, num_runs)
    results.append((exe_name, avg_runtime))

# Read the input from the text file
with open('pairs.txt', 'r') as f, open('runtimes.txt', 'w') as out_file:
    # Write the header to the output file
    out_file.write("Pair,Exe1,Time1,Exe2,Time2\n")
    
    for line in f:
        cols = line.split()

        # Extract the column values
        exe1 = cols[0]
        exe2 = cols[1]
        m = int(cols[2])
        n = int(cols[3])

        # Run the executables in separate threads and wait for them to complete
        results = []
        t1 = threading.Thread(target=run_exe_thread, args=(exe1, m, results))
        t2 = threading.Thread(target=run_exe_thread, args=(exe2, n, results))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        # Get the results and write them to the output file
        avg_runtime_exe1, avg_runtime_exe2 = results
        pair_name = f"[{exe1},{exe2}]"
        exe1_name, exe1_time = avg_runtime_exe1
        exe2_name, exe2_time = avg_runtime_exe2
        out_file.write(f"{pair_name},{exe1_name},{exe1_time:.2f},{exe2_name},{exe2_time:.2f}\n")
