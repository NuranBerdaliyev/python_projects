import asyncio


async def odd():
    for _ in range(100):
        if _%2!=0:
            print(_)
            await asyncio.sleep(0.1)

async def even():
    for _ in range(100):
        if _%2==0:
            print(_)
            await asyncio.sleep(0.1)

async def main():
    task_even=asyncio.create_task(even())
    task_odd=asyncio.create_task(odd())

    await task_even
    await task_odd

asyncio.run(main())