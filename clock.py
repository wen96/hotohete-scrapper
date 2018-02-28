import asyncio

import uvloop
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scrapper import scrap


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


if __name__ == "__main__":

    scheduler = AsyncIOScheduler()
    scheduler.add_job(scrap, 'interval', seconds=5)
    scheduler.start()

    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
