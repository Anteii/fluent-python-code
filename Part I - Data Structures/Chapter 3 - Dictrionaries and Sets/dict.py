import random


values = list(range(10))
d = {}

for ind, val in enumerate(reversed(values)):
    d[ind] = val
    
print(d.values()) # view (zero memory overhead)
print(list(reversed(d.values()))) # this view support reversed

## Remove duplicates from list
arr = random.choices(list(range(-3,3)), k=10)
print(f"Original array: {arr}")
print(f"Array with unique elements and preserved relative order: {dict.fromkeys(arr).keys()}")

## __missing__ hook
class MissingDict(dict):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def __missing__(self, key):
        self[key] = None
        return None
my_dict = MissingDict()
my_dict[1] = "hello"
my_dict[5] = "world"
my_dict["df"] = "!"
print(f"My dict before accessing missing key: {my_dict}")
print(f"Missing key ('rust') value: {my_dict["rust"]}")
print(f"My dict after accessing missing key: {my_dict}")
print(my_dict.get("c++", "missing"))
print(f"My dict after accessing missing key through get(): {my_dict}")

# NOTE: In CPython 3.6 compact memory layout was introduced in hash-tables
#       From python 3.7 it is an official language feature

# NOTE: Internals of dict and set: https://www.fluentpython.com/extra/internals-of-sets-and-dicts/
# NOTE: Because of how hash-table work in python, it is neccessary for hashable objects to has both __hash__ and __eq__
# NOTE: CPython uses Siphash algorithm
# NOTE: Memory overhead for python sets is significant, because it keeps 1/3 of hash-table buckets empty
# NOTE: dict uses only 1/3 of buckets, others remain empty
# NOTE: any fraction between 1/3 and 2/3 seems to work fine in practice
# NOTE: Key-sharing dictionary (python 3.3) (__dict__ for all instances of class have shared keys
#       or if it's not the case, __dict__ is rebuild as default dict)
# NOTE: from previous, all entries should have same attributes and attributes 
#       should be created in the __init__
