from rest_framework import serializers
from .models import *

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"

class ParameterSerializer(serializers.ModelSerializer):
    detail = DetailSerializer(read_only=True, many=True)
    class Meta:
        model = Parameter
        fields = "__all__"

class OfferSerializer(serializers.ModelSerializer):
    Parameter = ParameterSerializer(read_only=True, many=True)
    class Meta:
        model = Offer
        fields = '__all__'
