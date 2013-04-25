from collections import defaultdict, OrderedDict


def groupby(key_function, sequence):
    result = defaultdict(list)
    for element in sequence:
        result[key_function(element)].append(element)
    return result


def compose(function1, function2):
    return lambda arguments: function1(function2(arguments))


def iterate(function):
    composed_function = lambda arguments: arguments
    while True:
        yield composed_function
        composed_function = compose(function, composed_function)


def zip_with(function, *iterables):
    if len(iterables) == 0:
        return
    for arguments in zip(*iterables):
        yield function(*arguments)


def cache(function, cache_size):
    if cache_size <= 0:
        return function
    cache = OrderedDict()

    def cached_function(*args):
        if args not in cache:
            if len(cache) >= cache_size:
                cache.popitem(last=False)
            cache[args] = function(*args)
        return cache[args]

    return cached_function
