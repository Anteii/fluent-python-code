from typing import Callable


registered = []


def register(func: Callable):
    registered.append(func)
    
    return func

@register
def foo():
    ...

# decorators run in an import / run time
print(registered)