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

# debuging function call

def debug(fn):
    def wrapper(*args,**kwargs):
        args_value=', '.join(str(arg) for arg in args) # join is used to get itteratable 
        kwargs_value=' ,'.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling: {fn.__name__} with args:  {args_value} and kwargs: {kwargs_value}")
        return fn(*args,**kwargs)

    return wrapper

@debug
def greet(name,greetig="hello"):
    print(f"{greetig}, {name}")

greet("chai" ,greetig="namaste")