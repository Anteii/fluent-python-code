import asyncio
import random

from aiohttp import web

CITIES = ['Morocco', 'Moscow', 'New York', 'Boston', 'Tokyo', 'Torronto', 'Sydney']
NAMES = ['Jhon', 'Tom', 'Andrew', 'Chris', 'Elton', 'Mary', 'Chelsey', 'Alex']
SURNAMES = ['Prince', 'Gordon', 'Terry', 'Tanner', 'Whitney', 'Riddle', 'Li', 'Delacruz', 'Mcconnell']

async def get_city(request):
    await asyncio.sleep(0.5)
    return web.Response(text=random.choice(CITIES))

async def get_name(request):
    await asyncio.sleep(0.25)
    return web.Response(text=f'{random.choice(NAMES)} {random.choice(SURNAMES)}')

app = web.Application()
app.add_routes([web.get('/city', get_city),
                web.get('/name', get_name)])

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8080)