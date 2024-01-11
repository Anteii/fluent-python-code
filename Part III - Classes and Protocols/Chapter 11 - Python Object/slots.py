class A:
    __slots__ = ('x', 'y')
    # can't initialize x and y here
    # can do this in init or after object instantiating

class B(A):
    z: int = 4

class C:
    # Some tricks!
    __slots__ = ("__dict__", )
    
a = A()
b = B()
c = C()

a.x = 23
a.y = 5

print(a.x, a.y)
#print(a.__dict__) - raises Error

b.x = 1
print(b.x)
print(b.z)
b.t = 5
print(b.__dict__)

c.x = 123
print(c.x)