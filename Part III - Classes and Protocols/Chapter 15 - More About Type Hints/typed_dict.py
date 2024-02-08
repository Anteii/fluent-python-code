from datetime import datetime
from typing import TypedDict, _TypedDictMeta


class Car(TypedDict):
    model: str
    manufacturer: str
    horse_power: int
    sells_start_date: datetime

    def test(self):         # Typechecker goes nuts
        print('Test Func called')   #


#Car = TypedDict('Car', {'model': str, 'manufacturer': str, 'horse_power': int, 'sells_start_date': datetime})
car1 = Car(model = 'Viper', manufacturer = 'Dodge',
    horse_power = 500, sells_start_date = datetime.now())
print(type(car1))
print(type(TypedDict)) # Actually a function
# print(isinstance(car1, TypedDict)) # Error
# car1.test() # Error


## How TypedDict works under the hood

def base(typename, fields=None, /, *, total=True, **kwargs):
    
    if fields is None:
        fields = kwargs
    elif kwargs:
        raise TypeError("TypedDict takes either a dict or keyword arguments,"
                        " but not both")

    ns = {'__annotations__': dict(fields), '__module__': __name__}
    td = _TypedDictMeta(typename, (), ns, total=True)
    td.__orig_bases__ = (TypedDict,)
    
    return td

_base = type.__new__(_TypedDictMeta, 'base', (), {})
base.__mro_entries__ = lambda bases: (_base,)

class Car2(base):
    model: str
    manufacturer: str
    horse_power: int
    sells_start_date: datetime
    
    
car2 = Car2(model = 'Viper', manufacturer = 'Dodge',
    horse_power = 500, sells_start_date = datetime.now())

print(car2)


## Minified example
def base2(typename, fields=None, /, *, total=True, **kwargs):
    print('Called base2')
    return None

base2.__mro_entries__ = lambda bases: (object,) # Enough to be considered as a type (?)

class TestClass(base2):
    a: int
    b: int
    
print('Create TestClass object')    
# test_obj = TestClass(a=10, b=50) # Error
test_obj = TestClass()

print(test_obj)
