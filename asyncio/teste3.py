import asyncio

async def t1():
    print('t1 começou')
    await asyncio.sleep(2)
    print('t1 terminou')

async def t2():
    print('t2 começou')
    await asyncio.sleep(1)
    print('t2 terminou')



async def main():
    await asyncio.gather(
        t1(), t2()
    )

asyncio.run(main())
    