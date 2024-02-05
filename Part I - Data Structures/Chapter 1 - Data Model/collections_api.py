import collections.abc as abc
import typing

list_obj = list()
dict_obj = dict()
set_obj = set()
tuple_obj = tuple()
str_obj = str()

print(isinstance(list_obj, typing.Collection)) # True
print(isinstance(list_obj, abc.Collection)) # True

# from typing source
# Collection = _alias(collections.abc.Collection, 1)

print(isinstance(list_obj, abc.Mapping)) # False
print(isinstance(dict_obj, abc.Mapping)) # True

print(isinstance(set_obj, abc.Set)) # True
print(isinstance(set_obj, abc.MutableSet)) # True

print(isinstance(list_obj, abc.Sequence)) # True
print(isinstance(set_obj, abc.Sequence)) # False
print(isinstance(tuple_obj, abc.Sequence)) # True
print(isinstance(str_obj, abc.Sequence)) # True
print(isinstance(dict_obj, abc.Sequence)) # False

print(isinstance(tuple_obj, abc.Reversible)) # True, but tuple doesn't have __reversed__
print("Tuple __reversed__:", hasattr(tuple, "__reversed__"))

print(isinstance(dict_obj, abc.Reversible)) # True
print(isinstance(set_obj, abc.Reversible)) # False

dict_obj1 = {"a": 1, "r": 3, "x": 8}
print(dict_obj1)
print(list(reversed(dict_obj1))) # just keys: ['x', 'r', 'a']

# print(reversed(set_obj)) doesn't work

print(isinstance(tuple_obj, abc.Iterable)) # True
print(isinstance(dict_obj, abc.Iterable)) # True
print(isinstance(set_obj, abc.Iterable)) # True


print(isinstance(tuple_obj, abc.Container)) # True
print(isinstance(dict_obj, abc.Container)) # True
print(isinstance(set_obj, abc.Container)) # True