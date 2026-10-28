import time


def asghar(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time:.2f} seconds")
        return result

    return wrapper


@asghar
def sumNumbers():
    sum_numbers = 0
    for number in range(1, 1_000_00_001):
        sum_numbers += number
    return sum_numbers


print(sumNumbers())
