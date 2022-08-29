import concurrent.futures
from time import sleep

def dosomething(sec):
    print('thread has started')
    sleep(1)
    return f'completed in {sec}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(dosomething,1)
    f2 = executor.submit(dosomething,2)
    print(f1.result())
    print(f2.result())