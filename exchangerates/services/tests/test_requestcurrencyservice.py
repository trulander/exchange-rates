import json

from django.test import TestCase
from ..BusinessLogic.requestrurrencyrervice import RequestCurrencyService

from mock import patch, Mock

import requests

class ServiceTest(TestCase):
    """Test module for Request Currency Service"""

    def setUp(self) -> None:
        self._service = RequestCurrencyService()
        self.artificial = Mock()
        self.artificial.status_code = 200
        self.artificial.json = lambda : {'status': {'timestamp': '2021-09-27T20:38:50.528Z', 'error_code': 0, 'error_message': None, 'elapsed': 18,
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

    @patch('requests.get')
    def test_service_request(self, mock):
        mock.return_value = self.artificial

        correct_response = {'currency': 1, 'actual_date': '2021-09-27T20:38:50.528Z', 'price_usd': 42885.00187617128, 'percent_change_1h': -0.58936733, 'percent_change_24h': -1.66902867}

        result = self._service.request(id=1)

        self.assertEqual(result, correct_response)