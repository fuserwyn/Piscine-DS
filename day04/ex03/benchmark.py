import timeit
import sys
from functools import reduce
#globals:
func = str(sys.argv[1])
n = int(sys.argv[2])
num = int(sys.argv[3])
#loop:
def summ():
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i*i
#reduce:
def reduce_sum():
    lst = []
    for i in range(1, num + 1):
        lst.append(i)
    reduce(lambda summ, i: summ + i*i, lst)
#setup:
setup ="""
from __main__ import summ, reduce_sum
"""
#comparing_func:
def time_spent(func, n):
    if func == "loop":
        test = timeit.timeit(stmt = 'summ()', setup = setup, number = n)
    elif func == "reduce": 
        test = timeit.timeit(stmt = 'reduce_sum()', setup = setup, number = n)
    else: 
        raise ValueError("func must be: 'loop' or 'reduce'")
    print(test)
#main:     
if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise ValueError("Use 4 arguments")
    time_spent(func, num)