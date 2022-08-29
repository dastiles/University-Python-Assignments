import time
import math
import threading

start = time.perf_counter()


def runFunc(x):
    print(f'running {x}')
    time.sleep(2)
      
threads = []
for i in range(5):
   x = threading.Thread(target=runFunc, args=(i,))
   threads.append(x)
   x.start()
   
   
for index, thread in enumerate(threads):
    thread.join()
    
stop = time.perf_counter()


print(f'your code took {math.floor(stop-start)} seconds')