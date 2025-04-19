##### Simple Threading
import time
import threading

def Task1():
    time.sleep(4)
    print("Task1 Complete")
    
def Task2():
    time.sleep(6)
    print("Task2 Complete")
    
# Create Thread objects with the target functions
thread1 = threading.Thread(target=Task1)
thread2 = threading.Thread(target=Task2)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()


### Multi Processing CPU Bound Example
import multiprocessing
import time

def cpu_heavy_task():
    print("Process starting...")
    count = 0
    for _ in range(10**7):
        count += 1
    print("Process done.")

if __name__ == "__main__":
    start = time.time()

    processes = []
    for _ in range(4):
        p = multiprocessing.Process(target=cpu_heavy_task)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Total time with multiprocessing:", time.time() - start)