from multiprocessing import Process
import os, time
import math

def calc():
    for i in range(0, 1000000):
        math.sqrt(i)

if __name__ == "__main__":
    
    start = time.perf_counter()
    processes = []

    for i in range(os.cpu_count()):
        print('registering process %d' % i)
        processes.append(Process(target=calc))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end = time.perf_counter()
    print(f"Elapsed: {end - start: .3f} seconds")