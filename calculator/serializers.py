from django.db.models import fields, query
from rest_framework import serializers

from calculator.models import Calculate, Term, City


class CalculateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Calculate
        fields = ('id',
                  'cityto',
                  'cityfrom',
                  'weightto',
                  'weightfrom',
                  'inter_terminal',
                  'pickup',
                  'cargo_delivery',
                  'premium')




from rest_framework.negotiation import DefaultContentNegotiation

class IgnoreClientContentNegotiation(DefaultContentNegotiation):

    def select_renderer(self, request, renderers, format_suffix):
        """
        Select the first renderer in the `.renderer_classes` list.
        """
        # Allow URL style format override.  eg. "?format=json
        format_query_param = self.settings.URL_FORMAT_OVERRIDE
        format = format_suffix or request.query_params.get(format_query_param)
        request.query_params.get(format_query_param, format)

        if format is None:
            return (renderers[0], renderers[0].media_type)
        else:
            return DefaultContentNegotiation.select_renderer(self, request, renderers, format_suffix)


class TermSerializer(serializers.ModelSerializer):

    class Meta:
        model = Term
        fields = ('cityto',
                  'cityfrom',
                  'term_standart_to',
                  'term_standart_from',
                  'term_express_to',
                  'term_express_from')

class CitySerializer(serializers.Serializer):
    
    def to_internal_value(self, value):
        return value


class CityReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        read_only_fields = fields
        model = City

class CalculateSerializer(serializers.ModelSerializer):
    
    cityto = CitySerializer()
    cityfrom = CitySerializer()
    
    class Meta:
        model = Calculate
        exclude = ('id',)
        
    def create(self, validated_data):
        data = validated_data
        cityto_name = data.pop('cityto')
        cityfrom_name = data.pop('cityfrom')
        cityfrom = City.objects.filter(name=cityfrom_name).first()
        cityto = City.objects.filter(name=cityto_name).first()
        if not cityfrom:
            cityfrom = City.objects.create(name=cityfrom_name)
        if not cityto:
            cityto = City.objects.create(name=cityto_name)
        new_calc = Calculate(**data)
        new_calc.save()
        new_calc.cityto = cityto
        new_calc.cityfrom = cityfrom
        new_calc.save()
        return new_calc

