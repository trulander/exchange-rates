import json
from typing import Any, Union, Dict

import requests
from requests import Response

from django.conf import settings
from rest_framework import status

from Core.models.models.Currencies import Currencies
from Core.models.models.CurrencyRates import CurrencyRates
from Core.Serializers.serializers import CurrencyRatesSerializer
from Core.Serializers.serializers import CurrenciesSerializer


class RequestCurrencyService():

    def request(self, id: int) -> Union[Dict, None]:
        url: str = settings.URL_API_GET_ACTUALL_CURRENCY
        api_key: dict = settings.API_KEY
        params: dict = {
            **api_key,
            'id': id
        }

        result: Response = requests.get(url=url, params=params)
        if result.status_code == 200:
            print('status 200')
            decoded_data = self._json_request_decode(data_json=result.json(), id=id)
            return self._save_data(decoded_data)

        return None

    def _json_request_decode(self, data_json: json, id: int) -> dict[str, dict[str, Union[int, Any]]]:
        result = {
            'currency': {
                'id': id,
                'name': data_json['data'][str(id)]['name'],
                'slug': data_json['data'][str(id)]['slug'],
                'symbol': data_json['data'][str(id)]['symbol'],
            },

            'currency_rate': {
                'currency': id,
                'actual_date': data_json['status']['timestamp'],
                'price_usd': data_json['data'][str(id)]['quote']['USD']['price'],
                'percent_change_1h': data_json['data'][str(id)]['quote']['USD']['percent_change_1h'],
                'percent_change_24h': data_json['data'][str(id)]['quote']['USD']['percent_change_24h'],
            }
        }

        return result

    def _save_data(self, data: dict[str, dict[str, Union[int, Any]]]) -> json:

        currency_serializer = CurrenciesSerializer(data=data['currency'])
        currency_rate_serializer = CurrencyRatesSerializer(data=data['currency_rate'])

        if currency_serializer.is_valid():
            currency_serializer.save()
            print('curency object correct')
        else:
            print(currency_serializer.errors)

        if currency_rate_serializer.is_valid():
            print('currency_rate object correct')
            currency_rate_serializer.save()
        else:
            print(currency_rate_serializer.errors)

        return currency_rate_serializer.data
