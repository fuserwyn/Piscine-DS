import sys
import os

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        has_header = True
        if not os.access(self.path, os.R_OK):
            raise ValueError("420 times check before using input")
        with open(self.path, "r") as f:
            lines = []
            for line in f:
                lines += line.rstrip().split('\n') 
        if (len(lines) < 2):
            raise ValueError("We need more or equal than 1 lines")
        if lines[0] == "0,1" or lines[0] == "1,0":
            has_header = False
        if has_header and len(lines[0].split(',')) != 2:
            raise ValueError("wrong header")
        mod_lines = []
        if has_header:
            mod_lines = lines[1:]
        else:
            mod_lines = lines
        for line in mod_lines:
            if line != "0,1" and line != "1,0":
                raise ValueError("ooops, only 0,1 or 1,0 should be inside starting from first line")
        res = []
        for line in mod_lines:
            strs = line.split(',')
            numbers = []
            for number in strs:
                numbers.append(int(number))
            res.append(list(numbers))
        return res

    class Calculations:
        def counts(self, data):
            heads = 0
            tails = 0
            for pair in data:
                heads += pair[0]
                tails += pair[1]
            return heads, tails
        def fractions(self, heads, tails):
            first = heads * 100 / (heads + tails)
            second = tails * 100 / (heads + tails)
            return first, second


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError("No input file")
    outter = Research(sys.argv[1])
    print(outter.file_reader())
    inner = outter.Calculations()
    calc = inner.counts(outter.file_reader())
    print(calc[0], calc[1])
    frac = inner.fractions(calc[0], calc[1])
    print(frac[0], frac[1])