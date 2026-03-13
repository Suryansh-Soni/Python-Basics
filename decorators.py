#  timming function execution 
import time 

def timmer(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"{fn.__name__} ran in {end-start} time.")
        return result
    return wrapper

# use decorator to make every funtion pass from timmer()
@timmer
def example(n):
    time.sleep(n)

example(2)