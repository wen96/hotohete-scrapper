import asyncio

from api_resquester import request_api
from result_store import write_result


async def scrap():
    for i in range(1, 5):
        future = asyncio.Future()
        asyncio.ensure_future(request_api(future, i))
        future.add_done_callback(write_result)
