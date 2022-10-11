#!/usr/bin/env python

import os

def print_virtual_env():
    print("Your current virtual env is " + os.environ['VIRTUAL_ENV'])

if __name__ == '__main__':
    print_virtual_env()

# source ~/agidget/bin/activate
# zip agidget.zip ~/agidget