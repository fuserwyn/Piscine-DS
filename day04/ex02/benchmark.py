import timeit
import sys

mails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
n = 90000000 #calls numbers for main code
#main code 1:
def loop(mails):
    new_list_of_emails = []
    for mail in mails:
        if mail.endswith('@gmail.com'):
            new_list_of_emails.append(mail)   
#main code 2:
def comprehesion_list(mails):
    new_list_of_emails = [mail for mail in mails if mail.endswith('@gmail.com')]
#main code 3:
def map_loop(mails):
    new_list_of_emails = map(lambda mail: mail if mail.endswith('@gmail.com') else None, mails)
#main code 4:
def filtering(mails):
    new_list_of_emails = filter(lambda mail: mail if mail.endswith('@gmail.com') else None, mails)
#setup:
setup ="""
from __main__ import loop, comprehesion_list, map_loop, filtering
mails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
"""
#setting_func
def setting_func(native_func, n):
    if native_func == "loop":
        test = timeit.timeit(stmt = 'loop(mails)', setup = setup, number = n)
    elif native_func == "list_comprehension": 
        test = timeit.timeit(stmt = 'comprehesion_list(mails)', setup = setup, number = n)
    elif native_func == "map":
        test = timeit.timeit(stmt = 'map_loop(mails)', setup = setup, number = n)
    elif native_func == "filter":
        test = timeit.timeit(stmt = 'filtering(mails)', setup = setup, number = n)
    else: 
        raise ValueError("native func (second arg) must be: 'loop' or ' list_comprehension' or 'map' or 'filter'")
    print(test)
#main:    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("Use 3 arguments")
    setting_func(sys.argv[1], int(sys.argv[2]))
    