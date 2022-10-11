import timeit

n = 90000000 #calls numbers for main code
#main code 1:
def loop():
    mails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    new_list_of_emails = []
    for mail in mails:
        if mail.endswith('@gmail.com'):
            new_list_of_emails.append(mail)   
#main code 2:
def comprehesion_list():
    mails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    new_list_of_emails = [mail for mail in mails if mail.endswith('@gmail.com')]
#main code 3:
def map_loop():
    mails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    map_it = map(lambda mail: mail if mail.endswith('@gmail.com') else None, mails)

#setups:
setup_1 ="""
from __main__ import loop
"""
setup_2 ="""
from __main__ import comprehesion_list
"""
setup_3 ="""
from __main__ import map_loop
"""
#comparing:
def time_comparing():
    test1 = timeit.timeit(stmt = 'loop()', setup = setup_1, number = n)
    test2 = timeit.timeit(stmt = 'comprehesion_list()', setup = setup_2, number = n)
    test3 = timeit.timeit(stmt = 'map_loop()', setup = setup_3, number = n)
    if min(test1, test2) > test3:
        print(f'test time1: {test1}, test time2: {test2}, test time3: {test3}')
        print("it is better use a map")
    elif min(test1, test3) > test2:
        print(f'test time1: {test1}, test time2: {test2}, test time3: {test3}')
        print("it is better to use a list comprehension")
    elif min(test1, test2) > test1:
        print(f'test time1: {test1}, test time2: {test2}, test time3: {test3}')
        print("it is better use a loop")
    else: 
        print("you are lucky, it's probability is so low that if it'd happend this task doesn't make sense")
        
if __name__ == '__main__':
    time_comparing()
