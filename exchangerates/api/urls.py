from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'currencies', CurrenciesView, basename='currencies')
router.register(r'currenciesrates', CurrencyRatesView, basename='CurrenciesRates')


urlpatterns = [
    #path('currencies/<int:pk>/', CurrenciesDetail.as_view(), name="currenciesdetail"),
    url(r'^', include(router.urls)),
]