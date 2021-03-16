from functools import wraps


def call_counter(function):

    calls = 0

    @wraps(function)
    def wrapped(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f"Function {function.__name__} has been called {calls} times")

        result = function(*args, **kwargs)

        return result

    return wrapped

