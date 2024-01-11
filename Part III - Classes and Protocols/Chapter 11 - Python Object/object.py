class A:
    external_field: int = 1
    __internal_field: int = 1
    
    # How user wants to see an object
    def __str__(self) -> str:
        return f"A({self.external_field=})"
    
    # How developer wants to see an object
    def __repr__(self) -> str:
        return f"A({self.external_field=}; {self.__internal_field=})"

    def __bytes__(self) -> bytes:
        return f"A({self.external_field=}; {self.__internal_field=})".encode("utf-8")
    
a = A()

print(a) # calls a.__str__
print(repr(a))
print(bytes(a)) # calls __bytes__
#print(a.__internal_field) - raises Error
#name mangling
# __internal_field become _A__internal_field in __dict__
print(a._A__internal_field) # (in)correct way