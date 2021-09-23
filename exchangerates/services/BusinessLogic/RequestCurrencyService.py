import json

import requests
from requests import Response

# from Core.Models import *
# from Core.Models.Currencies import Currencies
# from Core.Models.CurrencyRates import CurrencyRates
from django.conf import settings

#from Core.Models.CurrencyRates import CurrencyRates
from Core.models.models import *


class RequestCurrencyService():

    def request(self, id: int) -> json:
        url: str = settings.URL_API_GET_ACTUALL_CURRENCY
        api_key: dict = settings.API_KEY
        params = {
            **api_key,
            'id': id
        }

        result: Response = requests.get(url=url, params=params)
        if result.status_code == 200:
            print('status 200')
            self._save_data()


        return result.json()

    def _save_data(self):
        pass
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def get_list(self, id: int):
        pass


    def get_latest_currency_rate(self, id: int) -> CurrencyRates:
        return CurrencyRates.objects.order_by('-actual_date').first()  #get(currency=id, date_added=)

