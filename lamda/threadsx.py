import time
import math
start = time.perf_counter()
def runFunc(x):
    print(f'running {x}')
    time.sleep(2)
      
    
for i in range(5):
    runFunc(i)
    
stop = time.perf_counter()

print(f'your code took {math.floor(stop-start)} seconds')