import asyncio
import random
from time import perf_counter
import typing

# This iterator is a naive implementation with added sleep
# Consequently not safe for concurrent environment
class ConsecutiveIterator:
    _data: list[int]
    _ind: int
    
    def __init__(self, size: int = 10) -> None:
        random.seed(42) # to ensure fair comparison
        self._data = list(range(size))
        self._ind = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self._ind >= len(self._data):
            raise StopAsyncIteration
        
        item = self._data[self._ind]
        
        await asyncio.sleep(random.random())
        
        self._ind += 1
        return item

# Iterator safe for concurrent iteration
class AsyncIterator:
    _data: list[int]
    _ind: int
    
    def __init__(self, size: int = 10) -> None:
        random.seed(42) # to ensure fair comparison
        
        self._data = list(range(size))
        self._ind = 0
        self._lock = asyncio.Lock()
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self._ind >= len(self._data):
            raise StopAsyncIteration
        
        await self._lock.acquire()
        
        item = self._data[self._ind]
        self._ind += 1
        
        self._lock.release()
        
        await asyncio.sleep(random.random())
        
        return item

# Sequentially iterate over items
async def async_for():
    async for item in ConsecutiveIterator():
        print(item, end=' ')
    print()
    # same with comprehension
    #print(' '.join([str(v) async for v in ConesuativeIterator()]))

# Eqaual to previous
async def unrolled_async_for():
    try:
        iterator = ConsecutiveIterator()
        while True:
            item_future = anext(iterator)
            item = await item_future
            print(item, end=' ')
    except StopAsyncIteration:
        print()

# If we try this we get infinite loop because
# each __anext__ update call state but was never awaited 
async def bad_gather1():
    try:
        iterator = ConsecutiveIterator()
        futures = []
        while True:
            item_future = anext(iterator)
            futures.append(item_future)
    except StopAsyncIteration:
        pass
    finally:
        print(' '.join((str(v) for v in await asyncio.gather(*futures))))
    
# Fixed example 3 but stil bad p
# print out 0 instead of 0 1 2 ...
# because AIter is not safe for concurrent iteration by design
async def bad_gather2():
    try:
        iterator = ConsecutiveIterator()
        futures = []
        for _ in range(10):
            item_future = anext(iterator)
            futures.append(item_future)
    except StopAsyncIteration:
        pass
    finally:
        print(' '.join((str(v) for v in await asyncio.gather(*futures))))

# Using safe iterator
async def correct_gather():
    try:
        iterator = AsyncIterator()
        futures = []
        for _ in range(10):
            item_future = anext(iterator)
            futures.append(item_future)
    except StopAsyncIteration:
        pass
    finally:
        print(' '.join((str(v) for v in await asyncio.gather(*futures))))

async def time_func(coro: typing.Coroutine, name: str):
    start = perf_counter()
    await coro
    print(f'{name} time: {perf_counter() - start}')

async def main(): 
    
    await time_func(async_for(), 'async_for')
    await time_func(unrolled_async_for(), 'unrolled_async_for')
    #await time_func(bad_gather1(), 'bad_gather1')
    await time_func(bad_gather2(), 'bad_gather2')
    await time_func(correct_gather(), 'correct_gather')
    
asyncio.run(main())