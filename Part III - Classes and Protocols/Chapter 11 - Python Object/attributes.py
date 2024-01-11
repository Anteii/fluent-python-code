class Boo:
    data = ["apple", "city", "raft"]
    
    def __init__(self, x = None) -> None:
        self.data.append(x) 


class Foo:
    a = Boo()
    b = Boo()
    
    def __init__(self, a: Boo | None) -> None:
        if a is not None:
            self.a = a


foo1 = Foo(Boo())
foo2 = Foo(None)

print(id(foo1.a), id(Foo.a)) # not same
print(id(foo2.a), id(Foo.a)) # same

print(f"{foo1.a=}")
print(f"{foo2.a=}")
print(f"{Foo.a=}")
print()

foo2.a = Boo()

print(f"{foo1.a=}")
print(f"{foo2.a=}")
print(f"{Foo.a=}")
print()

Foo.a = Boo()

print(f"{foo1.a=}")
print(f"{foo2.a=}")
print(f"{Foo.a=}")

foo3 = Foo(None)

print(foo3.a)

boo1 = Boo()
boo2 = Boo("trfg")

print(id(boo1.data), id(boo2.data)) # same

print(Boo.data) # ..., None, None, ..., None, 'trfg'