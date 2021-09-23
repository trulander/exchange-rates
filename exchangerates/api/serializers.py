from rest_framework import serializers

from Core.models.models.CurrencyRates import CurrencyRates
from Core.models.models.Currencies import Currencies


class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'


class CurrencyRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRates
        fields = '__all__'