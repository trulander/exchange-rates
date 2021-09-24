from django.urls import path, include

from .views import *

urlpatterns = [
    path('', api_root),

    path('ratescurrency/', CurrencyRatesView.as_view({
        'get': 'list'
    }), name="rates_currency_all"),

    path('ratescurrency/<int:pk>/', CurrencyRatesView.as_view({
        'get': 'get_all'
    }), name="rates_currency"),

    path('ratecurrency/<int:pk>/', CurrencyRatesView.as_view({
        'get': 'get_by_id'
    }), name="rate_currency_detail"),

    path('rate/<int:pk>/', CurrencyRatesView.as_view({
        'get': 'get_last_rate_by_currency_id'
    }), name="rate"),

    path('rate_latest/<int:pk>/', CurrencyRatesView.as_view({
        'get': 'get_latest_rate_currency_by_id'
    }), name="rate_latest"),



    path('currencies/', CurrenciesView.as_view({
        'get': 'get_all'
    }), name="currencies_list"),

    path('currencies/<int:pk>/', CurrenciesView.as_view({
        'get': 'get'
    }), name="currencies_detail"),
]