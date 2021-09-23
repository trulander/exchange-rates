from django.core.handlers.wsgi import WSGIRequest

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import mixins, GenericAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions

from .BusinessLogic.RequestCurrencyService import RequestCurrencyService
# from Core.Exceptions.Exceprions import IncorrectIdentityCurrencyException
from .serializers import *


class Currencies(viewsets.ModelViewSet):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    # def __init__(self, *args, **kwargs):
    #     self._service = RequestCurrencyService()
    #     super().__init__()
    #
    # def get(self, request, *args, **kwargs):
    #     result = self._service.request(1)
    #     return Response(result, status=status.HTTP_200_OK)
    #
    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Currencies(APIView):
#     _service: RequestCurrencyService
#     serializer_class = CurrenciesSerializer
#
#
#     def __init__(self, *args, **kwargs):
#         self._service = RequestCurrencyService()
#         super().__init__()
#
#     def get(self, request, *args, **kwargs):
#         result = self._service.request(1)
#         return Response(result, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrenciesDetail(APIView):
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
            data: CurrencyRates = self._service.get_latest_currency_rate(pk)
            serializer = self.serializer_class(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)






@api_view(['GET'])
def run_task(request: WSGIRequest, id: int = 1) -> Response:

    if type(id) is not int:
        raise IncorrectIdentityCurrencyException('Id must be as integer value')

    try:
        service: RequestCurrencyService = RequestCurrencyService()
        return Response(service.request(id), status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.args, status=status.HTTP_400_BAD_REQUEST)