import json

from django.contrib.auth.models import User
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse


from ..serializers import CurrencySerializer

# from mock import patch, Mock
from unittest.mock import patch, Mock
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase

from ..views import Currency


class GetLatestCurrencyTests(APITestCase):

    def setUp(self) -> None:
        user = User.objects.create_user(email=None, username='Admin', password='Admin')
        self._client = APIClient()
        self._client.force_authenticate(user=user)


    @patch('services.BusinessLogic.RequestCurrencyService.request')
    def test_requestcurrency_correct_response(self, mock):
        mock.return_value = {'id': 1, 'date_added': '2021-09-28T06:39:12.804133Z', 'actual_date': '2021-09-27T20:38:50.528000Z', 'price_usd': '42885.001876171280000', 'percent_change_1h': -0.58936733, 'percent_change_24h': -1.66902867, 'currency': 1}

        response = self._client.get(reverse('currency', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('services.BusinessLogic.RequestCurrencyService.request')
    def test_requestcurrency_incorrect_response(self, mock):
        mock.return_value = None
        response = self._client.get(reverse('currency', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @patch('services.BusinessLogic.RequestCurrencyService.request',
           side_effect=lambda x: (_ for _ in()).throw(Exception('test exceprion')))
    def test_requestcurrency_incorrect_business_logic_data(self, mock):
        response = self._client.get(reverse('currency', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data[0], 'test exceprion')
