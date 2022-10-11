#!/usr/bin/env python

import os
from pip._internal.operations import freeze

def install():
    os.system("pip install beautifulsoup4 pytest")

def pip_freeze_show():
    x = freeze.freeze()
    file = open("requirements.txt", "a")
    for p in x:
        print(p)
        file.write(p + "\n")

if __name__ == '__main__':
    os.environ['VIRTUAL_ENV']
    install()
    pip_freeze_show()
