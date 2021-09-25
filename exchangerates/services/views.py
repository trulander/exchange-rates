from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .BusinessLogic.requestrurrencyrervice import RequestCurrencyService
from .serializers import CurrencyRatesSerializer, CurrenciesSerializer


class Currency(APIView):
    _service: RequestCurrencyService
    serializer_class = CurrenciesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        self._service = RequestCurrencyService()
        super().__init__()

    def get(self, request, pk: int):
        if isinstance(pk, int):
            return Response('Id must be as integer value', status=status.HTTP_400_BAD_REQUEST)

        try:
            result = self._service.request(pk)
            if result is not None:
                return Response(result, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)