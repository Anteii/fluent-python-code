import asyncio
import itertools
import multiprocessing
import multiprocessing.synchronize
import threading
from time import sleep

symbols = ['\\', '|', '/', '—']

# Infinite spinner
def infinite_spinner():
    for symbol in itertools.cycle(symbols):
        print(symbol, end='\r')
        sleep(0.1)

# Asyncio demo
def async_spinner():
    async def spinner_task(msg: str):
        for symbol in itertools.cycle(symbols):
            print(symbol, end='\r')
            try:
                await asyncio.sleep(0.1)
            except asyncio.CancelledError:
                break
        print(f'Done: {msg}')
    
    async def spinner_supervisor():
        task = asyncio.create_task(spinner_task('async spinner'))
        await asyncio.sleep(3)
        task.cancel()
    
    asyncio.run(spinner_supervisor())
    
def threading_spinner():
    def spin(isDone: threading.Event, msg: str):
        for symbol in itertools.cycle(symbols):
            print(symbol, end='\r')
            sleep(0.1)
            if isDone.is_set():
                break
        print(f'Done: {msg}')
        
    isDone = threading.Event()
    
    thread = threading.Thread(target=spin, args=(isDone, "threading spinner"))
    
    thread.start()
    
    sleep(3)
    
    isDone.set()
    
    thread.join()

# Should be at top level
# So that it could be imported
def multiprocessing_spin(isDone: multiprocessing.synchronize.Event, msg: str):
        for symbol in itertools.cycle(['\\', '|', '/', '—']):
            print(symbol, end='\r')
            sleep(0.1)
            if isDone.is_set():
                break
        print(f'Done: {msg}')
        
def multiprocessing_spinner():
    
        
    isDone = multiprocessing.Event()
    
    proc = multiprocessing.Process(target=multiprocessing_spin, args=(isDone, "multiprocessing spinner"))
    
    proc.start()
    
    sleep(3)
    isDone.set()
    
    proc.join()
        
if __name__ == '__main__':
    multiprocessing_spinner()