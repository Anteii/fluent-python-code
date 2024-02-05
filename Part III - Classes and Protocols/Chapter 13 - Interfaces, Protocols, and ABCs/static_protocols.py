import abc
import typing

# "Dynamic" protocol
class DynamicProtocol:
    
    def foo(self):
        ...
    
    def bar(self):
        ...

class StaticProtocol(typing.Protocol):
    def foo(self):
        ...
    
    def bar(self):
        ...

@typing.runtime_checkable
class RuntimeStaticProtocol(typing.Protocol):
    def foo(self):
        ...
    
    def bar(self):
        ...

class TypeABC(abc.ABC):
    def foo(self):
        ...
    
    def bar(self):
        ...
        

class Type1:
    
    def foo(self):
        ...
    
    def bar(self):
        ...

class Type2(TypeABC):
    def foo(self):
        ...
    
    def bar(self):
        ...

def test_func1(arg1: DynamicProtocol):
    ...

def test_func2(arg1: StaticProtocol):
    ...

obj1 = Type1()
obj2 = Type2()


# test_func1(obj1) # Incompatible types
# test_func2(obj1) # OK

print(isinstance(obj1, DynamicProtocol))
# print(isinstance(obj1, StaticProtocol)) # TypeError: Instance and class checks can only be used with @runtime_checkable protocols
print(isinstance(obj1, RuntimeStaticProtocol))


print(isinstance(obj2, DynamicProtocol))
print(isinstance(obj2, RuntimeStaticProtocol))
print(isinstance(obj2, TypeABC))