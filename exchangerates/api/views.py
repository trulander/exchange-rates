from django.http import Http404
from django.shortcuts import render
from rest_framework import status, viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from Core.models.models.CurrencyRates import CurrencyRates
from Core.models.models.Currencies import Currencies
from .serializers import CurrencyRatesSerializer, CurrenciesSerializer


class CurrenciesView(viewsets.ModelViewSet):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CurrencyRatesView(viewsets.ViewSet):
    serializer_class = CurrencyRatesSerializer
    queryset = CurrencyRates.objects.all()

    def get_latest(self, request, pk: int):
        pass

    def list(self, request, pk: int = 1):
        current_rates = CurrencyRates.objects.filter(currency__id=pk).order_by('actual_date')
        if current_rates.count() < 1:
            return Response('Db doesn\'t have any data', status=status.HTTP_204_NO_CONTENT)

        serializer = CurrencyRatesSerializer(data=current_rates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, pk: int):
        try:
            currency_rate = CurrencyRates.objects\
                .filter(currency__id=pk)\
                .order_by('actual_date')\
                .filter()
        except CurrencyRates.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(data=currency_rate)
        return Response(serializer.data, status=status.HTTP_200_OK)
