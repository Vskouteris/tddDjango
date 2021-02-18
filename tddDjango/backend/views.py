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

#Views for getting (one or a list of) Offers,Parameters and Details
@api_view(['GET'])
def get_list_of_offers(request):
    data = Offer.objects.all()
    # print(data[::1])
    serializer = OfferSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_list_of_parameters(request):
    data = Parameter.objects.all()
    serializer = ParameterSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_list_of_details(request):
    data = Detail.objects.all()
    serializer = DetailSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_offer(request,args):
    offer = Offer.objects.get(id=args)
    serializer = OfferSerializer(offer)
    return Response(serializer.data)

@api_view(['GET'])
def get_parameter(request,args):
    parameter = Parameter.objects.get(id=args)
    serializer = ParameterSerializer(parameter)
    return Response(serializer.data)

@api_view(['GET'])
def get_detail(request,args):
    detail = Detail.objects.get(id=args)
    serializer = DetailSerializer(detail)
    return Response(serializer.data)

#Post views for creating a new Offer,Parameter or Detail
@api_view(['POST'])
def create_offer(request):
	serializer = OfferSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#Post views for updating a new Offer,Parameter or Detail