from rest_framework import serializers
#from Core.models.models import *
# from Core.Models.Currencies import Currencies
# from Core.Models.CurrencyRates import CurrencyRates
from Core.models.models import *


class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'


class CurrencyRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRates
        fields = '__all__'