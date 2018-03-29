import json

from api.models import Stat


def write_result(future):
    steam_id, cs_ingo = future.result()
    Stat.objects.create(user_id=steam_id, data=json.dumps(cs_ingo))
