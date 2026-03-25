import aiohttp, asyncio


urls = [
    "https://jamesclear.com/creative-thinking",
    "https://jamesclear.com/stay-on-the-bus"
    "https://jamesclear.com/one-sentence-habits"
]
async def fetch(session_async, url):
    async with session_async.get(url) as response:
        return await response.text()

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks=[fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

t=asyncio.run(main(urls))
print(t[0])
