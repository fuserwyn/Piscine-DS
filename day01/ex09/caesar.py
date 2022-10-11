import sys
from unittest import resultult
# https://dvsemenov.ru/shifr-cezarya-na-python-rukovodstvo-po-shifrovaniyu-teksta/

def encode_function(string, shift):
    result = ''
    lowercase = (''.join([chr(i) for i in range(97,123)]))
    uppercase = (''.join([chr(i) for i in range(65,91)]))
    printable = set(lowercase + uppercase + '0123456789' +
        r'!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~' + ' \t\n\r\f\v')
    for char in string:
        if char not in printable:
            raise ValueError('ooops')
        elif char in lowercase:
            index = lowercase.find(char)
            result += lowercase[(index + shift) % 26]
        elif char in uppercase:
            index = uppercase.find(char)
            result += uppercase[(index + shift) % 26]
        else:
            result += char
    return result


if __name__ == '__main__':
    if len(sys.argv) == 4:
        if sys.argv[1] == 'decode':
            print(encode_function(sys.argv[2], -int(sys.argv[3])))
        elif sys.argv[1] == 'encode':
            print(encode_function(sys.argv[2], int(sys.argv[3])))
        else:
            raise ValueError('choose: encode or decode')
    else:
        raise ValueError('use 4 args')