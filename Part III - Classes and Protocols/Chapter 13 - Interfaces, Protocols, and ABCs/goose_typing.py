import abc
import collections.abc

# Duck Typing
class TestSizable1:
    pass

class TestSizable2:
    def __len__(self):
        return 12.1
class TestSizable3:
    def __len__(self):
        return 12

obj1 = TestSizable1()
obj2 = TestSizable3()
obj3 = TestSizable3()


print(f'isinstance(obj1, abc.Sized) = {isinstance(obj1, collections.abc.Sized)}')
print(f'isinstance(obj2, abc.Sized) = {isinstance(obj2, collections.abc.Sized)}')
print(f'isinstance(obj3, abc.Sized) = {isinstance(obj3, collections.abc.Sized)}')
print()

# Goose typing
class AbstractGoose(abc.ABC):
    def quack(self):
        ...

class ConcreteGoose1:
    def quack(self):
        ...

class ConcreteGoose2(AbstractGoose):
    def quack(self):
        ...


obj1 = AbstractGoose() # You can create abstract object in python
obj2 = ConcreteGoose1()
obj3 = ConcreteGoose2()


print(f'isinstance(obj1, AbstractGoose) = {isinstance(obj1, AbstractGoose)}')
print(f'isinstance(obj2, AbstractGoose) = {isinstance(obj2, AbstractGoose)}')
print(f'isinstance(obj3, AbstractGoose) = {isinstance(obj3, AbstractGoose)}')
print()

AbstractGoose.register(ConcreteGoose1)

print(f'isinstance(obj2, AbstractGoose) = {isinstance(obj2, AbstractGoose)} (after AbstractGoose.register(ConcreteGoose1))')

