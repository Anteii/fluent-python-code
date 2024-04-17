import asyncio
from concurrent import futures
from time import perf_counter

import aiohttp
import httpx
import requests
from attr import dataclass


@dataclass
class Person:
    name: str
    city: str


def get_person_with_sync_requests(*args):
        full_name = requests.get('http://localhost:8080/name')
        city = requests.get('http://localhost:8080/city')
        return Person(full_name.text, city.text)

async def async_get_person_with_sync_requests(*args):
        async with (
            aiohttp.request('get', 'http://localhost:8080/name') as full_name,
            aiohttp.request('get', 'http://localhost:8080/city') as city,
        ):
            return Person(await full_name.text(), await city.text())

def test_threadpool_map(N_persons: int, N_workers: int | None, verbose: bool = False):
    
    worker_count = N_workers
    
    persons = []
    
    start = perf_counter()
        
    with futures.ThreadPoolExecutor(max_workers=N_workers) as executor:
        counts = [i for i in range(N_persons)]
        worker_count = executor._max_workers
        for i, person in enumerate(executor.map(get_person_with_sync_requests, counts)):
            persons.append(person)
            if verbose:
                print(f'{i:<10}{person.name:<25}{person.city}')
    
    total_time = perf_counter() - start
    
    if verbose:
        print(f'Threadpool({worker_count=}, map) time: {total_time}')
    
    return total_time

def test_threadpool_as_completed(N_persons: int, N_workers: int | None, verbose: bool = False):
    
    worker_count = N_workers
    
    persons = []
    
    start = perf_counter()
    
    with futures.ThreadPoolExecutor(max_workers=N_workers) as executor:
        worker_count = executor._max_workers
        fs = futures.as_completed((executor.submit(get_person_with_sync_requests) for _ in range(N_persons)))
        for i, f_person in enumerate(futures.as_completed(fs)):
            person = f_person.result()
            persons.append(person)
            if verbose:
                print(f'{i:<10}{person.name:<25}{person.city}')
    
    total_time = perf_counter() - start
    if verbose:
        print(f'Threadpool({worker_count=}, as_completed) time: {total_time}')
    
    return total_time

def test_processpool_as_completed(N_persons: int, N_workers: int | None, verbose: bool = False):
    
    worker_count = N_workers
    
    persons = []
    
    start = perf_counter()
    
    with futures.ProcessPoolExecutor(max_workers=N_workers) as executor:
        worker_count = executor._max_workers
        fs = futures.as_completed((executor.submit(get_person_with_sync_requests) for _ in range(N_persons)))
        for i, f_person in enumerate(futures.as_completed(fs)):
            person = f_person.result()
            persons.append(person)
            if verbose:
                print(f'{i:<10}{person.name:<25}{person.city}')
    
    total_time = perf_counter() - start
    if verbose:
        print(f'Threadpool({worker_count=}, as_completed) time: {total_time}')
    
    return total_time

async def async_download(N_persons: int):
    start = perf_counter()
    
    tasks = []
    persons = []
    
    for i in range(N_persons):
        task = asyncio.create_task(async_get_person_with_sync_requests())
        tasks.append(task)
    
    for person in await asyncio.gather(*tasks):
        persons.append(person)
        
    total_time = perf_counter() - start
    
    return total_time    

def run_times(fn, repeat, *args, **kwargs):
    mmin, mmax = float('+inf'), float('-inf')
    total_time = 0
    for _ in range(repeat):
        t = fn(*args, **kwargs)
        total_time += t
        mmin = min(mmin, t)
        mmax = max(mmax, t)
    
    print(f'{mmin=:.3f}\tmean={total_time / repeat:.3f}\t{mmax=:.3f}')
    
if __name__ == '__main__':
    num_persons = 100
    num_workers = 100
    max_proc = 20
    num_repeat = 3
    
    print('Run async with asyncio (create_task, gather)')
    run_times(lambda x: asyncio.run(async_download(x)), num_repeat, num_persons)
    
    print('Run threadpool with .map method')
    run_times(test_threadpool_map, num_repeat, num_persons, num_workers)
    
    print('Run threadpool with features.as_completed function')
    run_times(test_threadpool_as_completed, num_repeat, num_persons, num_workers)
    
    print('Run processpool with features.as_completed function')
    run_times(test_processpool_as_completed, num_repeat, num_persons, min(max_proc, num_persons))

# NOTE 1: map and as_completed display almost identical results with minor advantages in favour for as_completed
# NOTE 2: async version and threadpool also have almost identical results
# NOTE 3: ProcessPool is in lack here, because task is I/O bound, not CPU bound
    