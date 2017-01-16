def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result


def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)

from random import randint
max_size = 10**4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

import cProfile
import pstats

profiler = cProfile.Profile()
profiler.runcall(test)

stats = pstats.Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()


def insertion_sort2(data):
    result = []
    for value in data:
        insert_value2(result, value)
    return result

max_size = 10**4
data2 = [randint(0, max_size) for _ in range(max_size)]
test2 = lambda: insertion_sort2(data2)

from bisect import bisect_left

def insert_value2(array, value):
    i = bisect_left(array, value)
    array.insert(i, value)


profiler = cProfile.Profile()
profiler.runcall(test2)

stats = pstats.Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()


def my_utility(a, b):
    pass

def first_func():
    for _ in range(1000):
        my_utility(4, 5)

def second_func():
    for _ in range(10):
        my_utility(1, 3)

def my_program():
    for _ in range(20):
        first_func()
        second_func()

profiler = cProfile.Profile()
profiler.runcall(my_program)

stats = pstats.Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_callers()
