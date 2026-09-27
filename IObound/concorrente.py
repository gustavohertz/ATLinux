import time
import asyncio
import aiohttp

urls = ["http://example.com"] * 5

async def fetch(session, url):
    async with session.get(url) as response:
        await response.read()

async def download_concorrente(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

start = time.time()
asyncio.run(download_concorrente(urls))
print(f"Tempo Concorrente: {time.time() - start:.2f} segundos")