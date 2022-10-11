import sys

def client():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
                'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    return clients

def participant():
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                    'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    return participants

def recipient():
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return recipients

def first_list():
    clients = client()
    recipients = recipient()
    return list(set(clients) - set(recipients))

def second_list():
    clients = client()
    participants = participant()
    return list(set(participants) - set(clients))

def third_list():
    clients = client()
    participants = participant()
    return list(set(clients) - set(participants))

def marketing():
    if len(sys.argv) != 2:
        return (print('choose: first_list, second_list, third_list'))
    if (sys.argv[1] == 'first_list'):
        print(first_list())
    elif (sys.argv[1] == 'second_list'):
        print(second_list())
    elif (sys.argv[1] == 'third_list'):
        print(third_list())
    else:
       print('choose: first_list, second_list, third_list') 

if __name__ == '__main__':
    marketing()