import time

def calculate_decorator(func):
    def wrapper():
        time.sleep(3)
        print(func())
    return wrapper

@calculate_decorator
def hello():
    return 'Hello'
@calculate_decorator
def world():
    return 'World'

hello()