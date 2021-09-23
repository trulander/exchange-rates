from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

router = routers.DefaultRouter()
router.register(r'CurrenciesRates', CurrenciesDetail, basename='test')


urlpatterns = [
    #path('currencies/<int:pk>/', CurrenciesDetail.as_view(), name="currenciesdetail"),
    url(r'^', include(router.urls)),

    #path('runtask/', run_task, name='runtask')
]