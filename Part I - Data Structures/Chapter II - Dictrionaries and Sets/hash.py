# User-defined classes are hashable by default
class HasableUserClass:
    a: int = 3
    t: list[int] = [1, 2]

hashable_user_class_obj0 = HasableUserClass()
hashable_user_class_obj1 = HasableUserClass()

# if __eq__ is not defined, than check by id()
print(f"Is two object equal? {hashable_user_class_obj0 == hashable_user_class_obj1}")
print(f"Id: {id(hashable_user_class_obj0)}; Hash: {hash(hashable_user_class_obj0)} (before mutation)")

hashable_user_class_obj0.t.append(3)

print(f"Id: {id(hashable_user_class_obj0)}; Hash: {hash(hashable_user_class_obj0)} (after mutation)")

# Depending on the interpreter implementation id and value returned by the default hash __hash__
# can be equall

print(
    max(
        id(hashable_user_class_obj0) / hash(hashable_user_class_obj0), 
        hash(hashable_user_class_obj0) / id(hashable_user_class_obj0)))


# If we define __eq__, than we loose default hash implementation
class NotHashableUserClass:
    a: int = 3
    t: list[int] = [1, 2]
    
    def __eq__(self, o: object):
        if isinstance(o, NotHashableUserClass):
            if self.a == o.a and self.t == o.t:
                return True
        return False



not_hashable_user_class_obj = NotHashableUserClass()

try:
    print(hash(not_hashable_user_class_obj))
except TypeError:
    print(f"Hash function __hash__ = {not_hashable_user_class_obj.__hash__}")
    print(f"Object {not_hashable_user_class_obj=} is not hashable")
    