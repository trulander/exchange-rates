import datetime
import json
import time
from datetime import datetime
from decimal import Decimal

from django.test import TestCase
from rest_framework import status

from Core.Exceptions.exceprions import IncorrectResponseData
from ..BusinessLogic.requestrurrencyrervice import RequestCurrencyService
from Core.Models.models.сurrency import Currency
from Core.Models.models.currencyrate import CurrencyRate

from mock import patch, Mock

import requests

class ServiceTest(TestCase):
    """Test module for Request Currency Service"""

    def setUp(self) -> None:
        self._service = RequestCurrencyService()
        self._artificial = Mock()
        self._artificial.status_code = status.HTTP_200_OK
        self._artificial.json = lambda: {}


    @patch('requests.get')
    def test_request_correct_response(self, mock):
        self._artificial.json = lambda : {'status': {'timestamp': '2021-09-27T20:38:50.528Z', 'error_code': 0, 'error_message': None, 'elapsed': 18,
                    'credit_count': 1, 'notice': None}, 'data': {
            '1': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'num_market_pairs': 8678,
                  'date_added': '2013-04-28T00:00:00.000Z',
                  'tags': ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channels',
                           'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio',
                           'polychain-capital-portfolio', 'binance-labs-portfolio', 'arrington-xrp-capital',
                           'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio',
                           'dcg-portfolio', 'dragonfly-capital-portfolio', 'electric-capital-portfolio',
                           'fabric-ventures-portfolio', 'framework-ventures', 'galaxy-digital-portfolio',
                           'huobi-capital', 'alameda-research-portfolio', 'a16z-portfolio', '1confirmation-portfolio',
                           'winklevoss-capital', 'usv-portfolio', 'placeholder-ventures-portfolio',
                           'pantera-capital-portfolio', 'multicoin-capital-portfolio', 'paradigm-xzy-screener'],
                  'max_supply': 21000000, 'circulating_supply': 18827925, 'total_supply': 18827925, 'is_active': 1,
                  'platform': None, 'cmc_rank': 1, 'is_fiat': 0, 'last_updated': '2021-09-27T20:38:02.000Z', 'quote': {
                    'USD': {'price': 42885.00187617128, 'volume_24h': 30683726574.737343,
                            'percent_change_1h': -0.58936733, 'percent_change_24h': -1.66902867,
                            'percent_change_7d': -2.0244389, 'percent_change_30d': -11.92566283,
                            'percent_change_60d': 7.65903653, 'percent_change_90d': 17.91179659,
                            'market_cap': 807435598949.4121, 'market_cap_dominance': 42.6643,
                            'fully_diluted_market_cap': 900585039399.6, 'last_updated': '2021-09-27T20:38:02.000Z'}}}}}

        mock.return_value = self._artificial

        correct_result = {'id': 1, 'date_added': '2021-09-28T06:39:12.804133Z', 'actual_date': '2021-09-27T20:38:50.528000Z', 'price_usd': '42885.001876171280000', 'percent_change_1h': -0.58936733, 'percent_change_24h': -1.66902867, 'currency': 1}

        result = self._service.request(id=1)


        currency = Currency.objects.get()
        self.assertEqual(currency.id, 1)
        self.assertEqual(currency.name, 'Bitcoin')
        self.assertEqual(currency.slug, 'bitcoin')
        self.assertEqual(currency.symbol, 'BTC')

        currency_rate = CurrencyRate.objects.get()
        self.assertEqual(currency_rate.currency.id, correct_result['id'])
        # self.assertEqual(currency_rate.date_added, correct_response['date_added'])
        self.assertEqual(currency_rate.actual_date.ctime(), datetime.strptime(correct_result['actual_date'], "%Y-%m-%dT%H:%M:%S.%fZ").ctime() )
        self.assertEqual(round(currency_rate.price_usd, 10), round(Decimal(correct_result['price_usd']), 10))
        self.assertEqual(currency_rate.percent_change_1h, correct_result['percent_change_1h'])
        self.assertEqual(currency_rate.percent_change_24h, correct_result['percent_change_24h'])

        self.assertEqual(result['id'], correct_result['id'])
        self.assertEqual(result['actual_date'], correct_result['actual_date'])
        self.assertEqual(result['price_usd'], correct_result['price_usd'])
        self.assertEqual(result['percent_change_1h'], correct_result['percent_change_1h'])
        self.assertEqual(result['percent_change_24h'], correct_result['percent_change_24h'])
        self.assertEqual(result['currency'], correct_result['currency'])

    @patch('requests.get')
    def test_request_response_status_not_200(self, mock):
        self._artificial.status_code = status.HTTP_403_FORBIDDEN
        mock.return_value = self._artificial
        result = self._service.request(id=1)

        self.assertEqual(result, None)

    @patch('requests.get')
    def test_request_incorrect_response(self, mock):
        self._artificial.json = lambda : {}
        mock.return_value = self._artificial

        with self.assertRaises(IncorrectResponseData):
            result = self._service.request(id=1)