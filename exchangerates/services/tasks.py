from time import sleep
from typing import Dict

import requests

from celery import shared_task
import aiohttp
import asyncio

from services.BusinessLogic.RequestCurrencyService import RequestCurrencyService

@shared_task
def update_exchange(id: int, *args, **kwargs) -> Dict:
    service = RequestCurrencyService()
    result = service.request(id=id)
    print('complete task.....', result)
    return result
