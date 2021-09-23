from django.core.handlers.wsgi import WSGIRequest

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import mixins, GenericAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions

from .BusinessLogic.RequestCurrencyService import RequestCurrencyService
from Core.Serializers.serializers import CurrencyRatesSerializer
from Core.Serializers.serializers import CurrenciesSerializer
from Core.models.models.CurrencyRates import CurrencyRates
from Core.models.models.Currencies import Currencies


class Currency(APIView):
    _service: RequestCurrencyService
    serializer_class = CurrenciesSerializer

    def __init__(self, *args, **kwargs):
        self._service = RequestCurrencyService()
        super().__init__()

    def get(self, request, pk: int):

        if type(pk) is not int:
            return Response('Id must be as integer value', status=status.HTTP_400_BAD_REQUEST)
            # IncorrectIdentityCurrencyException('Id must be as integer value')

        try:
            result = self._service.request(pk)
            if result is not None:
                return Response(result, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)