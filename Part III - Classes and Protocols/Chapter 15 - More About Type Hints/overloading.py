from typing import overload

# First overload
@overload
def foo(a: int) -> int:
    return 1000 * a # ignored

# Second overload
@overload
def foo(a: int, b: int) -> int:
    return a * b # ignored

# Original implementation (what will be called)
def foo(a: int, b: int = 10) -> int:
    return a * b

print(foo(10))
print(foo(6, 1000))