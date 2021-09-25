from rest_framework import serializers
from Core.Models.models import *


class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'


class CurrencyRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRates
        fields = '__all__'