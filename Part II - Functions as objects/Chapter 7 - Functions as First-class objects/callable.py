from typing import Any


class CallableClass:
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("I was called!")
        

instance = CallableClass()

instance()


def foo():
    return "FooFunc"


# All the same
print(foo,                              foo()                           )
print(foo.__call__,                     foo.__call__()                  )
print(foo.__call__.__call__,            foo.__call__.__call__()         )
print(foo.__call__.__call__.__call__,   foo.__call__.__call__.__call__())
