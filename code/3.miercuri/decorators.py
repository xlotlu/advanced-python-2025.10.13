# scrieți o funcție `timeit2` care funcționează ca decorator
#
# funcția va printa timpul de execuție al funcției pe care o decorează

def timeit2(func):
    def innerfunc():
        print("sunt în decorator, yey!")
        return func()
    return innerfunc


def cache(func):
    inner_cache = {}

    def innerfunc():
        if func in inner_cache:
            return inner_cache[func]
        
        else:
            retval = func()
            inner_cache[func] = retval
            return retval
        
    return innerfunc    


import time 

def timeit2(func):
    def innerfunc(*args, **kwargs):
        start_time = time.time()
        
        rez = func(*args, **kwargs)

        end_time = time.time()
        diff = end_time - start_time

        print(f"Executed {func} in: {diff} seconds")

        return rez 
        
    return innerfunc

@timeit2
def sleepy(count=5):
    print('dorm un pic')
    sleep(count)
    print('gata')

    return 15


# Scrieți un decorator `repeat(num)`
def repeat(num):
    # num

    def decorator(func):
        def innerfunc(*args, **kwargs):
            
            for x in range(num):
                print("running", x)
                rez = func(*args, **kwargs)

            return rez 
            
        return innerfunc
    
    return decorator



def lru_cache(*args, maxsize=128):
    _cache = {}

    def decorator(func):
        def wrapper(*args, **kwargs):

            # logica de ....
            result = func(*args, **kwargs)
            # .... caching

            return result 

        return wrapper

    if args:
        if callable(args[0]):
            func = args[0]
            return decorator(func)
        else:
            maxsize = args[0]
            return decorator


# create a class-based decorator, `log()`
# that prints the function name, its parameters, and the execution time

import time

class log:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()

        # we join the representations of args
        # with a list of "kwarg=repr(value)"
        _allargs = [
            repr(v) for v in args
        ] + [
            f"{str(k)}={repr(v)}"
            for k, v in kwargs.items()
        ]
        
        print(
            "» %s(%s) :: %fs" % (
                self.func.__name__,
                ", ".join(_allargs),
                end_time - start_time
            )
        )

        return result

@log
def func(arg1, default="something"):
    return "i am been run"

func(5)
func(5, default="altceva")
func(5, "wow")


# modify the decorator above, to receive an optional parameter
# "target", defaulting to sys.stderr.
#
# if "target" is specified and is a string, open that file
# (in append mode) and write to it.
# 
# if specified and is a stream, use it directly.

# `log()`


import time
import sys

class log:
    def __init__(self, target=sys.stderr):
        if isinstance(target, str):
            # we must open the stream
            target = open(target, 'a')
            # (and it's ok to leave it open)
        self._target = target

    def __call__(self, func):
        # we return a new function that wraps `func`
        def inner(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            self._log(func, args, kwargs, end_time - start_time)

            return result
        
        return inner

    def _log(self, func, args, kwargs, duration):

        # we join the representations of args
        # with a list of "kwarg=repr(value)"
        _allargs = [
            repr(v) for v in args
        ] + [
            f"{str(k)}={repr(v)}"
            for k, v in kwargs.items()
        ]
        
        self._target.write(
            "» %s(%s) :: %fs\n" % (
                func.__name__,
                ", ".join(_allargs),
                duration
            )
        )
        self._target.flush()

@log()
def func(arg1, default="something"):
    time.sleep(.1)
    return "i am been run"

func(5, default="altceva")


# make `class log` be a decorator what works
# with or without the `target` parameter

import sys
import time

class log:
    def __init__(self, *args, target=sys.stderr):
        self.func = None

        if args:
            if callable(args[0]):
                # we received the func as first argument [§]
                # (i.e. we're being used as a decorator without arguments)
                self.func = args[0]
            
            else:
                target = args[0]

        if isinstance(target, str):
            target = open(target, 'a')
        
        self._target = target

    def __call__(self, *args, **kwargs):
        if self.func:
            # we are being run as a simple decorator, [§]
            # so we execute directly

            return self._executor(*args, **kwargs)

        else:
            # this is two-level decorator,
            # so we return a function

            self.func = args[0]
            return self._executor

    def _executor(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()

        self._log(self.func, args, kwargs, end_time - start_time)

        return result

    def _log(self, func, args, kwargs, duration):
        # we join the representations of args
        # with a list of "kwarg=repr(value)"
        _allargs = [
            repr(v) for v in args
        ] + [
            f"{str(k)}={repr(v)}"
            for k, v in kwargs.items()
        ]

        self._target.write(
            "» %s(%s) :: %fs\n" % (
                func.__name__,
                ", ".join(_allargs),
                duration
            )
        )
        self._target.flush()

"""
log(func)
# --> args = (func,)
#     __call__ (*args, **kwargs)

log()(func)
# --> args = ()
#     __call__ (func)

log("/fiș/ier.txt")(func)
# --> args = ("/fiș/ier.txt", )
#     __call__ (func)

with open("/fiș/ier.txt") as fp:
    log(fp)(func)
# --> args = (<_io.TextIOWrapper ...>)
#     __call__ (func)

log(target="/fiș/ier.txt")(func)
# --> args = ()
#     __call__ (func)
"""

@log
def funcx(arg1, default="something"):
    time.sleep(.1)
    return "i am been run"
funcx(5, default="altceva")


@log()
def funcy(arg1, default="something"):
    time.sleep(.1)
    return "i am been run"
funcy(5, default="altceva")


