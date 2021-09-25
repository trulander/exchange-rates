from django.urls import path, include
from .views import Currency


urlpatterns = [
    path('requestcurrency/<int:pk>/', Currency.as_view(), name="currency"),
]