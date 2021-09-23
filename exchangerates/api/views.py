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
from Core.Serializers.serializers import CurrenciesSerializer
from Core.Serializers.serializers import CurrencyRatesSerializer
from services.tasks import update_exchange


class CurrenciesView(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    def get_all(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



# class CurrenciesView(viewsets.ModelViewSet):
#     serializer_class = CurrenciesSerializer
#     queryset = Currencies.objects.all()
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CurrencyRatesView(viewsets.ViewSet):
    serializer_class = CurrencyRatesSerializer
    queryset = CurrencyRates.objects.all()

    @action('GET', detail=False, renderer_classes=[renderers.JSONRenderer])
    def get_latest_rate(self, request, pk: int):
        #result = update_exchange(id=pk)
        result = update_exchange.apply_async(ignore_result=False, kwargs=({'id': 1}))
        return Response(result.get(), status=status.HTTP_200_OK)

    @action('GET', detail=False, renderer_classes=[renderers.JSONRenderer])
    def list(self, request, pk: int = 1):
        current_rates = CurrencyRates.objects.filter(currency__id=pk).order_by('-actual_date')
        if current_rates.count() < 1:
            return Response('Db doesn\'t have any data', status=status.HTTP_204_NO_CONTENT)

        serializer = self.serializer_class(current_rates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action('GET', detail=False, renderer_classes=[renderers.JSONRenderer])
    def get_last_rate(self, request, pk: int):
        try:
            currency_rate = CurrencyRates.objects \
                .filter(currency__id=pk) \
                .order_by('-actual_date') \
                .first()
        except CurrencyRates.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(currency_rate)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action('GET', detail=False, renderer_classes=[renderers.JSONRenderer])
    def get(self, request, pk: int):
        try:
            currency_rate = CurrencyRates.objects.get(pk=pk)
        except CurrencyRates.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(currency_rate)
        return Response(serializer.data, status=status.HTTP_200_OK)
