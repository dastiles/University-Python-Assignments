
from threading import *
from time import *

start = perf_counter()
def myfunc(e):
    sleep(1)
    print(f'running threading {e}')
    
    
    
x1 = Thread(target=myfunc, args=('1') )
x2 = Thread(target=myfunc, args=('2') )
x3 = Thread(target=myfunc, args=('3') )
x4 = Thread(target=myfunc, args=('4') )
x5 = Thread(target=myfunc, args=('5') )


x1.start()
x2.start()
x3.start()
x4.start()
x5.start()


x1.join()
x2.join()
x3.join()
x4.join()
x5.join()




end = perf_counter()

print(f'this code took {end - start} seconds')
    