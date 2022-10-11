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
#setups:
setup_1 ="""
from __main__ import loop
"""
setup_2 ="""
from __main__ import comprehesion_list
"""
#comparing:
def time_comparing():
    test1 = timeit.timeit(stmt = 'loop()', setup = setup_1, number = n)
    test2 = timeit.timeit(stmt = 'comprehesion_list()', setup = setup_2, number = n)
    if test1 > test2:
        print(f'test time1: {test1}, test time2: {test2}')
        print("it is better to use a list comprehension")
    else:
        print(f'test time1: {test1}, test time2: {test2}')
        print("it is better use a loop")
    
if __name__ == '__main__':
    time_comparing()
    