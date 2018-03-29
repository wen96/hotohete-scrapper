import asyncio


async def request_api(future, i):
    await asyncio.sleep(3)
    future.set_result('Future {} is done!'.format(i))
