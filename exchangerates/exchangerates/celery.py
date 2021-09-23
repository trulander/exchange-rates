import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exchangerates.settings")

app = Celery()
app.conf.update(**settings.CELERY_CONFIGURATION)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
