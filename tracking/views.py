from rest_framework.views import APIView
from tracking.models import Tracking
from django.views.generic.list import ListView
from.serializers import TrackingSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


class Search(ListView):
    model = Tracking
    template_name = 'tracking.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        print(query)
        object_list = Tracking.objects.filter(tracking_number_client__icontains=query)
        return object_list
    

class Trak(APIView):
    
    def post(self, request):
        data = request.data
        tracking_number_client = data.get('trak', '')
        if tracking_number_client:
            object = Tracking.objects.filter(tracking_number_client=tracking_number_client)
            if object.exists() == False:
                message = {'status': 'trak not found'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            object = object.first()
            result = TrackingSerializer(object)
            return Response(result.data, status=status.HTTP_200_OK)
        message = {'status': 'no data'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
        

