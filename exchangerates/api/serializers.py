from rest_framework import serializers
from Core.models.models import *


class CurrenciesSerializer(serializers.ModelSerializer):
    currency = serializers.HyperlinkedIdentityField(many=False, view_name='rates_currency')
    link_detail = serializers.HyperlinkedIdentityField(many=False, view_name='currencies_detail', read_only=True, lookup_field='pk')

    class Meta:
        model = Currencies
        fields = ['id', 'link_detail', 'name', 'slug', 'symbol', 'currency']


class CurrencyRatesSerializer(serializers.ModelSerializer):
    link_detail = serializers.HyperlinkedIdentityField(many=False, view_name='rate_currency_detail', read_only=True, lookup_field='pk')
    currency = serializers.HyperlinkedRelatedField(many=False, view_name='rates_currency', read_only=True, lookup_field='pk')

    class Meta:
        model = CurrencyRates
        fields = ['id', 'link_detail', 'date_added', 'actual_date', 'price_usd', 'percent_change_1h', 'percent_change_24h', 'currency']