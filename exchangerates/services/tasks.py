from typing import Dict
from celery import shared_task

from services.BusinessLogic.RequestCurrencyService import RequestCurrencyService

@shared_task
def update_exchange(id: int, *args, **kwargs) -> Dict:
    service = RequestCurrencyService()
    result = service.request(id=id)
    return result
