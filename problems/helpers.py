from time import time

def time_it(some_function):

    def wrapper(*args, **kwargs):
        t1 = time()
        result = some_function(*args, **kwargs)
        end = time()-t1
        return result, end
    return wrapper


def load_text_file(f):
    with open(f) as file_:
        input = file_.readlines()

    input = [i.rstrip() for i in input]
    return input