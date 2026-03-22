import time, asyncio


async def k():
    for i in range(1000):
        await asyncio.sleep(0.1)
        print(i+1)

async def l():
    for i in range(1000):
        await asyncio.sleep(0.1)
        print(i)
    
async def go(): 
    await asyncio.gather(l(), k())

asyncio.run(go())