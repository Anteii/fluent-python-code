from typing import Callable


registry = set()

# If we don't want to modify behaviour, but rather add preliminary step
# We can just do something and return original function
def register(activate: bool = True):
    print("Run register")
    def decorate(func: Callable):
        print("Run decorator")
        if activate:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate

@register() # must be called (because it is factory)
def foo():
    print("Running: foo")

@register() # must be called (because it is factory)
def bar():
    print("Running: bar")

@register # if we don't invoke zoo we won't get error (factory will be called, but decorate - won't be called)
def zoo():
    print("Running: bar")

print(registry) # contains two functions

foo()
bar()