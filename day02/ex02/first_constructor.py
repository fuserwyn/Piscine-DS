import sys
import os

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        if not os.access(self.path, os.R_OK):
            raise ValueError("420 times check before using input")
        with open(self.path, "r") as f:
            lines = []
            for line in f:
                lines += line.rstrip().split('\n') 
        if lines[0] == "0,1" or lines[0] == "1,0" or lines[0] != "head,tail":
            raise ValueError("wrong header")
        for line in lines[1:]:
            if line != "0,1" and line != "1,0":
                raise ValueError("ooops, only 0,1 or 1,0 should be inside starting from first line")
        if (len(lines) < 2):
            raise ValueError("We need more or equal than 2 lines")
        return "\n".join(lines)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError("No input file")
    m = Research(sys.argv[1])
    print(m.file_reader())