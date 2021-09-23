from time import sleep
import requests

from celery import shared_task
import aiohttp
import asyncio

async def async_task():
    await asyncio.sleep(10)

@shared_task
def update_exchange():


    print('complete task.....')
    return True
