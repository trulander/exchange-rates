from unittest.mock import patch, Mock

from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase

from Core.Models.models.сurrency import Currency
from Core.Models.models.currencyrate import CurrencyRate


class APITests(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(email=None, username='Admin', password='Admin')
        self._client = APIClient()
        self._client.force_authenticate(user=user)

        currency = Currency.objects.create(
            **{'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin'}
        )

        currency_rate = CurrencyRate.objects.create(
            **{'date_added': '2021-09-28T06:39:12.804133Z', 'actual_date': '2021-09-27T20:38:50.528000Z', 'price_usd': '42885.001876171280000', 'percent_change_1h': -0.58936733, 'percent_change_24h': -1.66902867, 'currency_id': 1}
        )



    def test_ratescurrency(self):
        pass

    def test_ratescurrency_1(self):
        pass

    def test_ratecurrency_1(self):
        pass

    def test_lastrate_1(self):
        pass

    def test_latestrate_1(self):
        pass

    def test_currencies(self):
        pass

    def test_currencies_1(self):
        pass