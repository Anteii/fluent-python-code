import asyncio

#NOTE: can't use yield from in async generator
            
def simple_gen():
    for i in range(-10, 0, 1):
        yield i

async def simple_async_gen():
    for i in range(-10, 0, 1):
        yield i

async def asum():
    sum1 = 0
    async for v in simple_async_gen():
        sum1 += v
    
    sum2 = sum([v async for v in simple_async_gen()])
    
    assert sum1 == sum2
    
    return sum1

async def run_both():
    async_sum = asum()
    sync_sum = sum(simple_gen())
    
    print(f'Sum equals: {await async_sum == sync_sum}')
    
    
asyncio.run(run_both())