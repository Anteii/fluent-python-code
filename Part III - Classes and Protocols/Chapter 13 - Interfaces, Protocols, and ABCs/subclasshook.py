from abc import ABCMeta

# __subclasshook__ supported only by ABCs

class ABCType(metaclass=ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return True

class NotABCType:
    
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return True
 
class EmptyClass:
    pass



obj = EmptyClass()


print(isinstance(obj, EmptyClass))
print(isinstance(obj, ABCType))
print(isinstance(obj, NotABCType))