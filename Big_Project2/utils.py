import time

class LogIterator:
    def __init__(self, filename):
        self._file=open(filename, 'r')

    def __iter__(self):
        return self
    
    def __next__(self):
        line=self._file.readline()
        if not line:
            self._file.close()
            raise StopIteration
        return line.strip()


def measure_time(func):
    def wrapper(*args, **kwargs):
        t0=time.time()
        result=func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-t0:.5f}s")
        return result
    return wrapper