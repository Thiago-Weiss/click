import asyncio

async def main():
    task = asyncio.create_task(other_function())
    
    print('a')
    await asyncio.sleep(2)
    print('b')

    valor = await task
    print(valor)

async def other_function():
    print('1')
    await asyncio.sleep(1)
    print('2')
    return 10


asyncio.run(main())
    