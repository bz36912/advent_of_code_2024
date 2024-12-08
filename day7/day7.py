import numpy as np
import threading
from queue import Queue
sem = threading.Semaphore()
jobs = Queue()
total = 0

def decimal_to_base3(n):
    sign = '-' if n<0 else ''
    n = abs(n)
    if n < 3:
        return str(n)
    s = ''
    while n != 0:
        s = str(n%3) + s
        n = n//3
    return sign+s

def compute_line():
    global total
    while True:
        line = jobs.get()
        if line == "":
            print("exiting a thread")
            exit()
        parts = line.split(":")
        target = int(parts[0])
        operator = parts[1].strip().split(" ")
        operator = [int(op) for op in operator]

        for i in range(3**(len(operator)-1)):
            # binary = bin(i)[2:].zfill(len(operator)-1)
            base3 = decimal_to_base3(i).zfill(len(operator)-1)
            curVal = operator[0]
            for idx, bit in enumerate(base3):
                if bit == '0':
                    curVal += operator[idx+1]
                elif bit == '1':
                    curVal *= operator[idx+1]
                else:
                    strVal = str(curVal) + str(operator[idx+1])
                    curVal = int(strVal)
            if curVal == target:
                sem.acquire()
                print(f"{line.strip()} using {base3}")
                total += target
                sem.release()
                break

NUM_WORKERS = 5
threads = []
for i in range(NUM_WORKERS):
    t = threading.Thread(target=compute_line)
    threads.append(t)
    t.start()

file = open("day7/dummy.txt", "r")

for aline in file:
    jobs.put(aline)

for i in range(NUM_WORKERS):
    jobs.put("") # empty signal the worker to end/exit the thread
for worker in threads:
    worker:threading.Thread
    worker.join()

print(f"total: {total}")
print("end")