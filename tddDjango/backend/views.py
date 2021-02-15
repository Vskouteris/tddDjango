from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.
def home_page(request):
    offers = Offer.objects.all()
    parameters = Parameter.objects.all()
    details = Detail.objects.all()
    context = {'offers':offers, 'parameters':parameters, 'details':details}
    return render(request, 'backend/home.html',context)

@api_view(['GET'])
def testDatabase(request):
    data = Parameter.objects.all()
    
    serializer = ParameterSerializer(data, many=True)
    return Response(serializer.data)