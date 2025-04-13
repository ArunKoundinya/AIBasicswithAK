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