from time import sleep
from threading import Thread
from tkinter import Y

def task():
    print('Starting a task....')
    sleep(1)
    print('done')
    
process_1 = Thread(target=task)
process_2 = Thread(target=task)

process_2.start()
process_1.start()

print('it is a multi threads program')


import time

print('this print statement will print immediately')
time.sleep(5)
print('this print statement will print 5 seconds later')








from threading import Thread
import time


def function_with_daemon():
    print('this function is running in the background')
    time.sleep(2)
    
# create three threads
x = Thread(target=function_with_daemon, daemon= True)
y = Thread(target=function_with_daemon, daemon= True)
z = Thread(target=function_with_daemon, daemon= True)

# start the threads
x.start()
y.start()
z.start()

# wait for the threads to finish
x.join()
y.join()
z.join()

# 

add = lambda x ,y, z: x+y+z
print(add(5,5,5))
# output => 15
