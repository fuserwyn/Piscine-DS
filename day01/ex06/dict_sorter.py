def data():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    return list_of_tuples

def sort_dict_by_v(x):
    sorted_list_of_tuples = sorted(x.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {k: v for k, v in sorted_list_of_tuples}
    return sorted_dict

def checker(x):
    new_dict = {}
    k = list(x.keys())
    v = list(x.values())
    for i in range(len(k) - 1):
        if (v[i] == v[i + 1]):
            if k[i + 1] < k[i]:
                k[i] = k[i + 1]
                k[i + 1] = k[i]
    new_dict = dict(zip(k, v))
    return new_dict

def output():
    my_dict = dict(data())
    for k, v in my_dict.items():
        my_dict[k] = int(v)
    sorted_dict = sort_dict_by_v(my_dict)
    sorted_dict = checker(sorted_dict)
    for key in sorted_dict.keys():
        print(key)

if __name__ == '__main__':
    output()