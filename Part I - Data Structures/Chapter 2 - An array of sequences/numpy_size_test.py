import numpy as np
from sys import getsizeof, stderr
from itertools import chain
from collections import deque
try:
    from reprlib import repr
except ImportError:
    pass


# https://stackoverflow.com/a/27559899/11131433
def total_size(o, handlers={}, verbose=False):
    """ Returns the approximate memory footprint an object and all of its contents.

    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:

        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}

    """
    def dict_handler(d: dict):
        return chain.from_iterable(d.items())
    
    all_handlers = {tuple: iter,
                    list: iter,
                    deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                   }
    all_handlers.update(handlers)     # user handlers take precedence
    seen = set()                      # track which object id's have already been seen
    default_size = getsizeof(0)       # estimate sizeof object without __sizeof__

    def sizeof(o):
        if id(o) in seen:       # do not double count the same object
            return 0
        seen.add(id(o))
        s = getsizeof(o, default_size)

        if verbose:
            print(s, type(o), repr(o), file=stderr)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)

np_int = np.array([1, 2, 3])
np_float = np.array([1.0, 2.0, 3.0])
np_arr_mixed = np.array([1, 2.3, "a", 1, 2.3, "a", 1, 2.3, "a", 1, 2.3, "a"])
list_obj = [1, 2.3, "a", 1, 2.3, "a", 1, 2.3, "a", 1, 2.3, "a"]

print(f"Array ({np_int.dtype}): {np_int}")
print(f"nbytes: {np_int.nbytes}, sizeof: {getsizeof(np_int)}")
print("#"*10)

print(f"Array ({np_float.dtype}): {np_float}")
print(f"nbytes: {np_float.nbytes}, sizeof: {getsizeof(np_float)}")
print("#"*10)

print(f"Array ({np_arr_mixed.dtype}): {np_arr_mixed}")
print(f"nbytes: {np_arr_mixed.nbytes}, sizeof: {getsizeof(np_arr_mixed)}")
print("#"*10)

print(f"List: {list_obj}")
print(f"sizeof: {getsizeof(list_obj)}")