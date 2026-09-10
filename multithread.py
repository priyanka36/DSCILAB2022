#!/usr/bin/env python3
"""Threads that perform calculations."""

import os
import threading
import time
import math


# A function that performs a simple calculation repeatedly
def calculate():
    result = 0
    for i in range(1, 1000000):
        result += math.sqrt(i)
    return result


# A function that runs the calculation in a loop for 1 minute
def cpu_calculator():
    start_time = time.time()

    while time.time() - start_time < 60:  # Run for 1 minute
        calculate()


# Display information about this process
print('\nProcess ID: ', os.getpid())
print('Thread Count: ', threading.active_count())

for thread in threading.enumerate():
    print(thread)


print('\nStarting 12 CPU Calculators...')

threads = []

for i in range(12):
    thread = threading.Thread(target=cpu_calculator)
    threads.append(thread)
    thread.start()


# Allow time for all threads to start
time.sleep(1)


# Display information about this process after threads have started
print('\nProcess ID: ', os.getpid())
print('Thread Count: ', threading.active_count())

for thread in threading.enumerate():
    print(thread)


# Wait for all threads to finish
for thread in threads:
    thread.join()


# Display information about this process after threads finish
print('\nProcess ID: ', os.getpid())
print('Thread Count: ', threading.active_count())

for thread in threading.enumerate():
    print(thread)