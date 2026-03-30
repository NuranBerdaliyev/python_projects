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
    t0=time.time()
    def wrapper(*args, **kwargs):
        
        result=func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-t0:.50f}s")
        return result
    return wrapper