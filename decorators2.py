import time


def decorator(func):
    def wrapper():
        print('decoration begins')
        func()
        print('decoration ends')
    return wrapper


def duration_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        duration = time.time() - start_time
        print(f'duration {duration}')
    return wrapper


def twice_decorator(func):
    def wrapper():
        func()
        func()
    return wrapper


@twice_decorator
@decorator
@duration_decorator
def func():
    print('function')
    time.sleep(1)


# func = decorator(func)
func()
