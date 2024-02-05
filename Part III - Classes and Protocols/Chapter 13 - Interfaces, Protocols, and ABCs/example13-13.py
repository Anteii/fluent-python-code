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
    def __mul__(self: 'AlternativeRepeatable', 
                repeat_count: int, /) -> 'AlternativeRepeatable': 
        ...

# Python 12
@runtime_checkable
class GenericRepeatable[Y](Protocol):
    def __mul__(self: Y, repeat_count: int, /) -> Y: 
        ...

RT = TypeVar('RT', bound=Repeatable)

def double(x: RT) -> RT:
    return x * 2

def triple(x: Repeatable) -> Repeatable:
    return x * 3

def quadriple(x: AlternativeRepeatable) -> AlternativeRepeatable:
    return x * 4

def quintiple(x: GenericRepeatable) -> GenericRepeatable:
    return x * 5

x = 5
print(isinstance(x, Repeatable))
print(isinstance(5, GenericRepeatable))
double(x)       # OK
triple(x)       # OK
quadriple(x)    # OK
quintiple(x)    # Why not OK?
