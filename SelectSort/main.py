import time
import random
class TimerError(Exception):


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):

        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")

def selectSort(tab, n):
    for x in range(n-1):
        minimum = x
        for j in range(x+1, n):
            if tab[j] < tab[minimum]:
                minimum = j
        if x != minimum:
            pom = tab[x]
            tab[x] = tab[minimum]
            tab[minimum] = pom

def selectSortReverse(tab, n):
    for x in range(n-1):
        minimum = x
        for j in range(x+1, n):
            if tab[j] > tab[minimum]:
                minimum = j
        if x != minimum:
            pom = tab[x]
            tab[x] = tab[minimum]
            tab[minimum] = pom


array = [1,2,3]
i = 0

while i < 100000:
    array.append(random.randint(-1000000,1000000))
    i = i + 1
t = Timer()
t.start()
selectSort(array, 100000)
t.stop()
t.start()
selectSort(array,100000)
t.stop()
selectSortReverse(array, 100000)
t.start()
selectSortReverse(array,100000)
t.stop()


