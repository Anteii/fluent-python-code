from __future__ import print_function
import ctypes


# float consists of three fields C structure:
# ob_refcnt - number of references to this object
# ob_type - pointer to the type of the object
# ob_fval - floating point value (type double)

f = 5.2
f_address = id(f)
ob_type_addr = f_address + 8 * ctypes.sizeof(ctypes.c_byte)
ob_fval_addr = f_address + 2 * 8 * ctypes.sizeof(ctypes.c_byte)

ob_refcnt = ctypes.c_long.from_address(f_address)
ob_type = ctypes.c_int32.from_address(ob_type_addr)
ob_fval = ctypes.c_double.from_address(ob_fval_addr)

print(ob_refcnt) # c_long(3)
print(ob_type)
print(ob_fval) # c_double(5.2)


# so tuple of floats takes three times more memory than 
# float array of the same size


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

import sys
import array

array_obj = array.array("d", [])
list_obj = []
tuple_obj = tuple()

arr_delta = []
tuple_delta = []
list_delta = []

for i in range(16):
    s1 = total_size(array_obj)
    array_obj.append(float(i))
    s2 = total_size(array_obj)
    arr_delta.append(s2-s1)
    
    s1 = total_size(tuple_obj)
    tuple_obj = tuple([float(j) for j in range(i+1)])
    s2 = total_size(tuple_obj)
    tuple_delta.append(s2-s1)
    
    s1 = total_size(list_obj)
    list_obj.append(float(i))
    s2 = total_size(list_obj)
    list_delta.append(s2-s1)

print("Float size: ", sys.getsizeof(1.0), total_size(1.0))  # 24 24
print("Array size: ", sys.getsizeof(array_obj), total_size(array_obj)) # 208 208
print("Tuple size: ", sys.getsizeof(tuple_obj), total_size(tuple_obj)) # 168 552
print("List size: ", sys.getsizeof(list_obj), total_size(list_obj)) # 184 568

print("Array allocations: ", arr_delta)
print("Tuple allocations: ", tuple_delta)
print("List allocations: ", list_delta)

# Array allocations:  [32, 0, 0, 0, 32, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0]
# Tuple allocations:  [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]
# List allocations:  [56, 24, 24, 24, 56, 24, 24, 24, 88, 24, 24, 24, 24, 24, 24, 24] 

# Tuple allocation is 32 = 28 (PyFloatObject) + 8 (64-bit pointer)
# List allocate 56 = 4 * 8 (4 64-bit pointers) + 24 (PyFloatObject)
