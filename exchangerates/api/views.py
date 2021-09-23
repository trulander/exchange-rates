from django.http import Http404
from django.shortcuts import render
from rest_framework import status, viewsets, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import renderers

from Core.models.models.CurrencyRates import CurrencyRates
from Core.models.models.Currencies import Currencies
from .serializers import CurrencyRatesSerializer, CurrenciesSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('currenciesdetail',args=({'pk':1}), request=request, format=format),

    })


class CurrenciesView(viewsets.ModelViewSet):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CurrencyRatesView(viewsets.ViewSet):
    serializer_class = CurrencyRatesSerializer
    queryset = CurrencyRates.objects.all()

    def get_latest(self, request, pk: int):
        pass

    @action('GET', detail=False, renderer_classes=[renderers.JSONRenderer])
    def list(self, request, pk: int = 1):
        current_rates = CurrencyRates.objects.filter(currency__id=pk).order_by('-actual_date')
        if current_rates.count() < 1:
            return Response('Db doesn\'t have any data', status=status.HTTP_204_NO_CONTENT)

        serializer = self.serializer_class(current_rates, many=True)
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
