class A:
    field1: int
    field2 = 2
    

a = A()
#print(a.field1) - raises AttributeError
print(a.__annotations__) # has field1