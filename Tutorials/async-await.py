import asyncio

async def main():
    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(1)
    print("B")
    result = await task
    print(result)

async def other_function():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return 10

asyncio.run(main())