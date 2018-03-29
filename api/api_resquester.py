import logging

from api.steam_api_service import SteamAPIService


async def request_api(future, steam_id):
    result = SteamAPIService().get_cs_info(steam_id)
    logging.info('Info for user {} retrieved!'.format(steam_id))
    future.set_result((steam_id, result))
