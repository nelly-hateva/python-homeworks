from collections import defaultdict
from collections import deque


def groupby(key_function, sequence):
    result = defaultdict(list)
    for element in sequence:
        key = key_function(element)
        result[key].append(element)
    return result


def iterate(function):
    iterated_function = lambda *args: len(args) == 1 and args[0] or args
    while True:
        yield iterated_function
        iterated_function = \
            (lambda f: (lambda *args: function(f(*args))))(iterated_function)


def zip_with(function, *iterables):
    if len(iterables) == 0:
        return []
    minimum_length = min(list(map(len, iterables)))
    for i in range(0, minimum_length):
        arguments = [x[i] for x in iterables]
        result = function(*arguments)
        yield result


def cache(function, cache_size):
    cache = {}
    count_size = 0
    queue = deque([], cache_size)

    def function_cached(*args):
        nonlocal count_size
        nonlocal cache_size

        if args in cache:
            return cache[args]
        else:
            return_value = function(*args)
            if count_size == cache_size:
                cache.pop(queue.popleft())
                count_size -= 1
            cache[args] = return_value
            queue.append(args)
            count_size += 1
            return return_value

    return function_cached
