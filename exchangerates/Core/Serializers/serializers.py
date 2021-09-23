from rest_framework import serializers
from Core.models.models import *


class CurrenciesSerializer(serializers.ModelSerializer):
    currency_rates = serializers.HyperlinkedIdentityField(many=True, view_name='rate_currency_detail')
    currency = serializers.HyperlinkedIdentityField(many=False, view_name='rates_currency')
    id = serializers.HyperlinkedRelatedField(many=False, view_name='currencies_detail', read_only=True, lookup_field='pk')


    class Meta:
        model = Currencies
        fields = ['id', 'name', 'slug', 'symbol', 'currency', 'currency_rates']


class CurrencyRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRates
        fields = '__all__'