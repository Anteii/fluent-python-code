from typing import TypeVar, Protocol, runtime_checkable

# There we use TypeVars to designate that
#  __mul__ return object of the same type

T = TypeVar('T')

@runtime_checkable
class Repeatable(Protocol):
    # Changed signature from (self: T, repeat_count: int) to this
    # Pylance is triggered by absent of / argument in the end
    def __mul__(self: T, repeat_count: int, /) -> T: 
        ...


@runtime_checkable
class AlternativeRepeatable(Protocol):
    # Changed signature from (self: T, repeat_count: int) to this
    # Pylance is triggered by absent of / argument in the end
    def __mul__(self, repeat_count: int, /) -> 'AlternativeRepeatable': 
        ...

RT = TypeVar('RT', bound=Repeatable)

def double(x: RT) -> RT:
    return x * 2

def triple(x: Repeatable) -> Repeatable:
    return x * 3

def quadriple(x: AlternativeRepeatable) -> AlternativeRepeatable:
    return x * 4

x = 5
print(isinstance(x, Repeatable))
double(x)       # OK
triple(x)       # OK
quadriple(x)    # OK
