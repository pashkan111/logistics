from rest_framework import serializers
from .models import Office
from calculator.models import City


class CitySerializer(serializers.Serializer):
    def to_internal_value(self, value):
        return value


class OfficeSerializer(serializers.Serializer):
    
    city = CitySerializer()
    name = serializers.CharField()
    phone = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    schedule = serializers.CharField(required=False)
        
    def create(self, validated_data):
        city_name = validated_data.pop('city')
        city = City.objects.filter(name=city_name).first()
        # if not city.exists():
        #     city = City.objects.create(name=city_name)
        new_office = Office(**validated_data)
        new_office.save()
        new_office.city = city
        new_office.save()
        return new_office
        
        
        
        
        