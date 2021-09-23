from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import *

# router = routers.DefaultRouter()
# router.register(r'currencies', CurrenciesView, basename='currencies')
#router.register(r'currenciesrates', CurrencyRatesView, basename='CurrenciesRates')


urlpatterns = [
    path('ratescurrency/<int:pk>/', CurrencyRatesView.as_view({
        'get': 'list'
    }), name="rates_currency"),

    path('ratecurrency/<int:pk>/', CurrencyRatesView.as_view({
        'get': 'get'
    }), name="rate_currency_detail"),

    path('rate/<int:pk>/', CurrencyRatesView.as_view({
        'get': 'get_last_rate'
    }), name="rate"),

    path('rate_latest/<int:pk>/', CurrencyRatesView.as_view({
        'get': 'get_latest_rate'
    }), name="rate_latest"),


    path('currencies/', CurrenciesView.as_view({
        'get': 'get_all'
    }), name="currencies_list"),

    path('currencies/<int:pk>/', CurrenciesView.as_view({
        'get': 'get'
    }), name="currencies_detail"),

    # url(r'^', include(router.urls)),
]