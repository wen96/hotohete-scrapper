import asyncio

from api.api_resquester import request_api
from api.result_store import write_result


async def scrap():
    user_ids = [
        '76561198007546519',  # clapton
        '76561198318172023',  # avid
        '76561198012260260',  # alf
        '76561198004689578',  # cereal
        '76561197960559825',  # sata
        '76561198037335727',  # negro
        '76561197979169931',  # jc
        '76561198036008541',  # antonio
    ]
    futures = []
    for user_id in user_ids:
        future = asyncio.Future()
        future.add_done_callback(write_result)
        asyncio.ensure_future(request_api(future, user_id))
        futures.append(future)
    await asyncio.wait(futures)
