import sys
import psutil

def generator(file):
    for line in open(file, "r"):
        yield line

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError("Wrong number of arguments")
    for line in generator(sys.argv[1]):
        pass
    process = psutil.Process()
    print(f'Peak memory usage = {process.memory_info().rss / 1024 ** 3:0.3f} GB')
    cpu_times = process.cpu_times()
    print(f'User Mode Time + System Mode Time = {cpu_times.user + cpu_times.system:0.2f}s')
