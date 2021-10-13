from django.urls import path, include

from .views import *

urlpatterns = [
    path('', api_root),

    path('ratecurrency/all/', CurrencyRateView.as_view({
        'get': 'list'
    }), name="rates_currency_all"),

    path('ratecurrency/all/<int:pk>/', CurrencyRateView.as_view({
        'get': 'get_all'
    }), name="rates_currency"),

    path('ratecurrency/<int:pk>/', CurrencyRateView.as_view({
        'get': 'get_by_id'
    }), name="rate_currency_detail"),

    path('ratecurrency/last/<int:pk>/', CurrencyRateView.as_view({
        'get': 'get_last_rate_by_currency_id'
    }), name="rate"),

    path('ratecurrency/latest/<int:pk>/', CurrencyRateView.as_view({
        'get': 'get_latest_rate_currency_by_id'
    }), name="rate_latest"),



    path('currency/', CurrencyView.as_view({
        'get': 'get_all'
    }), name="currencies_list"),

    path('currency/<int:pk>/', CurrencyView.as_view({
        'get': 'get'
    }), name="currency_detail"),
]