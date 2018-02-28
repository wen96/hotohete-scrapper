import asyncio


async def request_api(future, i):
    await asyncio.sleep(1 + i)
    future.set_result('Future {} is done!'.format(i))
