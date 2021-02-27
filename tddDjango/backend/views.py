from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .forms import *

# Create your views here.
def home_page(request):
	offers = Offer.objects.all()
	parameters = Parameter.objects.all()
	details = Detail.objects.all()

	formDetail = DetailForm()
	formParameter = ParameterForm()
	formOffer = OfferForm()

	context = {'offers':offers, 'parameters':parameters, 'details':details,
				"formOffer":formOffer, "formParameter": formParameter, 	"formDetail":formDetail
	}
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

@api_view(['POST'])
def create_parameter(request):
	serializer = ParameterSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def create_detail(request):
	serializer = DetailSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#Post views for updating a new Offer,Parameter or Detail

@api_view(['POST'])
def update_offer(request, pk):
	offer = Offer.objects.get(id=pk)
	serializer = OfferSerializer(instance=offer, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def update_parameter(request, pk):
	parameter = Parameter.objects.get(id=pk)
	serializer = ParameterSerializer(instance=parameter, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def update_detail(request, pk):
	detail = Detail.objects.get(id=pk)
	serializer = DetailSerializer(instance=detail, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#DELETE views for deleting an old Offer,Parameter or Detail

@api_view(['GET','DELETE'])
def deleteOffer(request, pk):
	offer = Offer.objects.get(id=pk)
	offer.delete()
	return Response('Offer succsesfully deleted!')

@api_view(['GET','DELETE'])
def deleteParameter(request, pk):
	parameter = Parameter.objects.get(id=pk)
	parameter.delete()
	return Response('Parameter succsesfully deleted!')

@api_view(['GET','DELETE'])
def deleteDetail(request, pk):
	detail = Detail.objects.get(id=pk)
	detail.delete()
	return Response('Detail succsesfully deleted!')