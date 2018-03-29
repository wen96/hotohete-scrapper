import asyncio

import uvloop

from api.scrapper import scrap
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Start a consumer'

    def handle(self, *args, **options):
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(scrap())
        loop.close()
