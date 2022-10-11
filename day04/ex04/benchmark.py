#!/usr/bin/env python

import collections
import timeit
import random
from collections import Counter

def randomizer():
    randomizer_list = [random.randint(0, 100) for _ in range(1000000)]
    return randomizer_list

def dict_out_ofthe_list(randomizer_list):
    keys = [key for key in range(0, 101)]
    values = []
    for k in keys:
        sum = 0
        for n in randomizer_list:
            if n == k:
                sum = sum + 1
        values.append(sum)
    return dict(zip(keys, values))

def top_ten(randomizer_list):
    dict = dict_out_ofthe_list(randomizer_list)
    top = sorted(dict.items(), key=lambda item: item[1], reverse=True) #сортируем по 01 элемента списка кортежей
    print(top)
    print('\n')
    keys = [k[0] for k in top]
    print(keys)
    return keys[:10]

def counter(randomizer_list):
    cnt = collections.Counter(randomizer_list)
    return cnt

def counter_most_common(randomizer_list):
    c = counter(randomizer_list)
    top = c.most_common(10)
    return [k[0] for k in top]

def time_res():
    r_list = randomizer()
    res1 = timeit.timeit(f'dict_out_ofthe_list({r_list})', 'from __main__ import dict_out_ofthe_list', number=1)
    res2 = timeit.timeit(f'counter({r_list})', 'from __main__ import counter', number=1)
    res3 = timeit.timeit(f'top_ten({r_list})', 'from __main__ import top_ten', number=1)
    res4 = timeit.timeit(f'counter_most_common({r_list})', 'from __main__ import counter_most_common', number=1)
    print(f'my function: {res1}\nCounter: {res2}')
    print(f'my top: {res3}\nCounter\'s top: {res4}')

if __name__ == '__main__':
    # time_res()
    r = randomizer()

    print(dict_out_ofthe_list(r))
    print(counter(r))
    print(top_ten(r))
    print(counter_most_common(r))