from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from consignment.models import OrderConsignment, OrderStatusConsignment
from consignment.serializers import OrderConsignmentSerializer, OrderStatusConsignmentSerializer


@api_view(['GET', 'DELETE'])
def consignment_list_order(request):
    if request.method == 'GET':
        order_consignments = OrderConsignment.objects.all()
        order_consignments_serializer = OrderConsignmentSerializer(order_consignments, many=True)
        return JsonResponse(order_consignments_serializer.data, safe=False)

    elif request.method == 'DELETE':
        count = OrderConsignment.objects.all().delete()
        return JsonResponse({'message': '{} Заявки были успешно удалены!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def create_consignment_orderstatus(request):
    if request.method == 'GET':
        orderstatus_consignments = OrderStatusConsignment.objects.all()
        orderstatus_consignments_serializer = OrderStatusConsignmentSerializer(orderstatus_consignments, many=True)
        return JsonResponse(orderstatus_consignments_serializer.data, safe=False)

    elif request.method == 'POST':
        orderstatus_consignment_data = JSONParser().parse(request)
        orderstatus_consignments_serializer = OrderStatusConsignmentSerializer(data=orderstatus_consignment_data, many=True)
        if orderstatus_consignments_serializer.is_valid():
            orderstatus_consignments_serializer.save()
            return JsonResponse(orderstatus_consignments_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(orderstatus_consignments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def consignment_detail_orderstatus(request, pk):
    try:
        orderstatus_consignment = OrderStatusConsignment.objects.get(pk=pk)
    except OrderStatusConsignment.DoesNotExist:
        return JsonResponse({'message': 'Накладной не существует'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        orderstatus_consignment_data = JSONParser().parse(request)
     
        orderstatus_consignments_serializer = OrderStatusConsignmentSerializer(orderstatus_consignment, data=orderstatus_consignment_data)
        if orderstatus_consignments_serializer.is_valid():
            orderstatus_consignments_serializer.save()
            return JsonResponse(orderstatus_consignments_serializer.data, {'message': 'Статус накладной обновлен!'}, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(orderstatus_consignments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateOrder(APIView):
    def post(self, request):
        data = request.data
        
    

