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
    # groups = serializers.PrimaryKeyRelatedField(many=True)
    parameters = serializers.CharField(source='get_all_parameters_in_offer', read_only=True)
    class Meta:
        model = Offer
        fields = '__all__'
