from numpy.lib.function_base import append
from simplequeue import SimpleQueue
from timeit import timeit

TIMES = 1

def measure(function):
    time = timeit(function, number=TIMES)
    time_str = f"Execution time: {time/TIMES:.7f} seconds"
    print(time_str)

""" def add_value_simpleq(self):
    append_queue = SimpleQueue.append(self,value= "Aniruddh")

def remove_value_simpleq(self):
    popleft_queue = SimpleQueue.popleft(self)
    print (popleft_queue) """


measure(SimpleQueue.append(self=SimpleQueue, value="Anirddh"))
measure(SimpleQueue.popleft)


