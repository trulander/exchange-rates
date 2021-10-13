from rest_framework import serializers
from Core.Models.models import *


class CurrencySerializer(serializers.ModelSerializer):
    currency = serializers.HyperlinkedIdentityField(many=False, view_name='rates_currency')
    link_detail = serializers.HyperlinkedIdentityField(many=False, view_name='currency_detail', read_only=True, lookup_field='pk')

    class Meta:
        model = Currency
        fields = ['id', 'link_detail', 'name', 'slug', 'symbol', 'currency']


class CurrencyRateSerializer(serializers.ModelSerializer):
    link_detail = serializers.HyperlinkedIdentityField(many=False, view_name='rate_currency_detail', read_only=True, lookup_field='pk')
    currency = serializers.HyperlinkedRelatedField(many=False, view_name='rates_currency', read_only=True, lookup_field='pk')

    class Meta:
        model = CurrencyRate
        fields = ['id', 'link_detail', 'date_added', 'actual_date', 'price_usd', 'percent_change_1h', 'percent_change_24h', 'currency']