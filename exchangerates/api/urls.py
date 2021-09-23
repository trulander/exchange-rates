from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'currencies', CurrenciesView, basename='currencies')
#router.register(r'currenciesrates', CurrencyRatesView, basename='CurrenciesRates')

currenciesrates = CurrencyRatesView.as_view({
    'get': 'list'
})

urlpatterns = [
    path('currenciesrates/<int:pk>/', currenciesrates, name="currenciesdetail"),
    url(r'^', include(router.urls)),
]