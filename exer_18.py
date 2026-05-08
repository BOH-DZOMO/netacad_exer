import time as t
def make_multiplier(n):
    def wrapper(m):
        return m*n
    return wrapper

mul = make_multiplier(5)
print(mul(5))


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = t.perf_counter()
        result = func(*args, **kwargs)
        end_time = t.perf_counter()
        time_diff = end_time-start_time
        return f"The code ran for {time_diff} seconds and the result is {result}"
    
    return wrapper


@timer
def operate():
    sum = 0
    for i in range(100000000):
        sum+=1

    return sum

period = operate()
print(period)


def log_call():
    def wrapper(*args ):
        pass
