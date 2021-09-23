from django.db.models import Count 
from django.views import generic
from rest_framework.response import Response
from office.models import City, Office
from django.shortcuts import render
from .serializers import OfficeSerializer
from rest_framework import views

class OfficeView(generic.ListView):
    template_name = 'offices.html'
    queryset = City.objects.annotate(num=Count('office_of_city')).filter(num__gt=0).order_by('name')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # cities = Office.objects.raw('''
        #         SELECT distinct c.id, c.name 
        #         FROM office_office o 
        #         LEFT JOIN calculator_city c 
        #         ON o.city_id=c.id 
        #         ORDER BY c.name DESC
        # ''')
        # data['offices'] = Office.objects.all().select_related('city')
        data['cities'] = self.queryset
        return data
    
class OfficeApiView(views.APIView):
    def post(self, request):
        import time
        s = time.time()
        for i in request.data:
            serializer = OfficeSerializer(data=i)
            if not serializer.is_valid():
                message = {'status': 'no'}
                print(serializer.errors)
                return Response(message)
            serializer.save()
        f = time.time()
        message = {'status': 'ok'}
        return Response(message)
            

