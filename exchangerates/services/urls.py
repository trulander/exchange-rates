from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import Currency

# router = routers.DefaultRouter()
# router.register(r'currency', Currency, basename='currency')


urlpatterns = [
    path('currency/<int:pk>/', Currency.as_view(), name="currency"),
    # url(r'^', include(router.urls)),
]