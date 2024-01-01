# Because hash(1) == hash(1.0) and 1 == 1.0
s = {1.0, 2.0, 3.0}
s.add(1)
print(s) # {1.0, 2.0, 3.0}

d = {1: "a", 5: 1}

print(d.keys() & {1, 2, 3}) # can't do {1, 2} & []

a, b = [1, 2], [3, 4]
s = {*a, *b}
print(s)

# NOTE: sets uses hashmap but don't keep order
# NOTE: dict views implement some sets methods
#       dict_items can be used as set in case, if all values are hashable
#       if not, TypeError will be thrown