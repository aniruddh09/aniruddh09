from timeit import timeit
from collections import deque

SIZE = 10000
TIMES = 10

def measure(function):
    time = timeit(function, number=TIMES)
    time_str = f"Execution time: {time/TIMES:.7f} seconds"
    settings = f"(SIZE: {SIZE}, TIMES: {TIMES}, {function.__name__})"
    print(time_str, settings)

def fifo_list():
    a_list = list(range(SIZE))
    while a_list:
        a_list.pop(0)


def fifo_deque():
    a_queue = deque(range(SIZE))
    while a_queue:
        a_queue.popleft()

measure(fifo_list)
measure(fifo_deque)