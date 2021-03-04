from functools import wraps


def print_function_name(function):

    @wraps(function)
    def wrapped(*args, **kwargs):

        print(f'Executing: ', function.__name__)
        result = function(*args, **kwargs)

        return result

    return wrapped
