from itertools import count

#### Example 1: simple coroutune
def create_averager_online():
    total: float = 0.0
    count: int = 0
    average: float = 0.0
    
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

producer = count()
averager = create_averager_online()
averager.send(None)

for term in iter(lambda: next(producer), 5):
    print(f'{term=}')
    print(averager.send(term))


#### Example 2: coroutine with return statement
class Sentinel:
    pass

def create_averager_offline():
    total: float = 0.0
    count: int = 0
    average: float = 0.0
    
    while True:
        term = yield
        if isinstance(term, Sentinel):
            break
        total += term
        count += 1
        average = total / count
    
    return average

producer = count()
averager = create_averager_offline()
averager.send(None)

for term in iter(lambda: next(producer), 5):
    print(f'{term=}')
    averager.send(term) # None

try:
    averager.send(Sentinel())
except StopIteration as se:
    print(se.value)

#### Example 3: coroutines are not async
def printing_coroutine():
    while True:
        yield
        for i in range(3):
            print(f"hello from coroutine {i}")
cr = printing_coroutine()
cr.send(None)
for i in range(4):
    cr.send(i)
    print("hello from main")
    
#### Example 4: get returned value from coroutine in coroutine
def get_max_from_pair():
    global_max = float('-inf')
    pair_max = None
    while True:
        t1 = yield pair_max
        if isinstance(t1, Sentinel):
            break
        t2 = yield
        if isinstance(t2, Sentinel):
            break
        pair_max = max(t1, t2)
        global_max = max(global_max, pair_max)
        
    return global_max

def get_max_from_seqs():
    result = yield from get_max_from_pair()
    return result

producer = count()
cr = get_max_from_seqs()
cr.send(None)

for term in iter(lambda: next(producer), 6):
    print(f'{term=}')
    cr.send(term) # None

try:
    cr.send(Sentinel())
except StopIteration as se:
    print(se.value)
    