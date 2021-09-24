from rest_framework import status, viewsets, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import action
from rest_framework import renderers

from Core.models.models.CurrencyRates import CurrencyRates
from Core.models.models.Currencies import Currencies
from .serializers import CurrenciesSerializer, CurrencyRatesSerializer
from services.tasks import update_exchange


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'ratescurrency': reverse('rates_currency_all', request=request, format=format),
        'currencies': reverse('currencies_list', request=request, format=format)
    })

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



class CurrencyRatesView(viewsets.GenericViewSet,
                        mixins.ListModelMixin):
    serializer_class = CurrencyRatesSerializer
    queryset = CurrencyRates.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @action('GET', detail=False, renderer_classes=[renderers.JSONRenderer])
    def get_latest_rate_currency_by_id(self, request, pk: int):
        result = update_exchange.apply_async(ignore_result=False, kwargs=({'id': pk}))
        return Response(result.get(), status=status.HTTP_200_OK)

    @action('GET', detail=False, renderer_classes=[renderers.JSONRenderer])
    def get_all(self, request, pk: int = 1, *args, **kwargs):
        self.queryset = CurrencyRates.objects.filter(currency__id=pk).order_by('-actual_date')
        return self.list(request, *args, **kwargs)

    @action('GET', detail=False, renderer_classes=[renderers.JSONRenderer])
    def get_last_rate_by_currency_id(self, request, pk: int, *args, **kwargs):
        try:
            currency_rate = CurrencyRates.objects \
                .filter(currency__id=pk) \
                .order_by('-actual_date') \
                .first()
        except CurrencyRates.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(currency_rate, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action('GET', detail=False, renderer_classes=[renderers.JSONRenderer])
    def get_by_id(self, request, pk: int):
        try:
            currency_rate = CurrencyRates.objects.get(pk=pk)
        except CurrencyRates.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(currency_rate, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
