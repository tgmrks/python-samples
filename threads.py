from threading import Thread
import os, time
import math

def calc():
    for i in range(0, 1000000):
        math.sqrt(i)

start = time.perf_counter()
threads = []

for i in range(os.cpu_count()):
    print('registering thread %d' % i)
    threads.append(Thread(target=calc))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = time.perf_counter()
print(f"Elapsed: {end - start: .3f} seconds")