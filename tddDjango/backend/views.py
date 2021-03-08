from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics



# Create your views here.
def home_page(request):
	offers = Offer.objects.all()
	parameters = Parameter.objects.all()
	details = Detail.objects.all()

	formDetail = DetailSerializer()
	formParameter = ParameterSerializer()
	formOffer = OfferSerializer()

	context = {'offers':offers, 'parameters':parameters, 'details':details,
				"formOffer":formOffer, "formParameter": formParameter, 	"formDetail":formDetail
	}
	return render(request, 'backend/home.html',context)


class OfferViewList(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					generics.GenericAPIView):

	queryset= Offer.objects.all()
	serializer_class=OfferSerializer

	def get(self,request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class ParameterViewList(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					generics.GenericAPIView):

	queryset= Parameter.objects.all()
	serializer_class=ParameterSerializer

	def get(self,request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class DetailViewList(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					generics.GenericAPIView):

	queryset= Detail.objects.all()
	serializer_class=DetailSerializer

	def get(self,request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)		

#Offer get update delete
class OfferRUD(generics.RetrieveUpdateDestroyAPIView):
	queryset=Offer.objects.all()
	serializer_class= OfferSerializer

#Parameter get update delete
class ParameterRUD(generics.RetrieveUpdateDestroyAPIView):
	queryset=Parameter.objects.all()
	serializer_class= ParameterSerializer

#Detail get update delete
class DetailRUD(generics.RetrieveUpdateDestroyAPIView):
	queryset=Detail.objects.all()
	serializer_class= DetailSerializer

# @api_view(['GET'])
# def get_parameter(request,args):
#     parameter = Parameter.objects.get(id=args)
#     serializer = ParameterSerializer(parameter)
#     return Response(serializer.data)

# @api_view(['GET'])
# def get_detail(request,args):
#     detail = Detail.objects.get(id=args)
#     serializer = DetailSerializer(detail)
#     return Response(serializer.data)

# @api_view(['POST'])
# def update_parameter(request, pk):
# 	parameter = Parameter.objects.get(id=pk)
# 	serializer = ParameterSerializer(instance=parameter, data=request.data)
# 	if serializer.is_valid():
# 		serializer.save()
# 	else:
# 		return Response({'serializer': serializer})
# 	return Response(serializer.data)

# @api_view(['POST'])
# def update_detail(request, pk):
# 	detail = Detail.objects.get(id=pk)
# 	serializer = DetailSerializer(instance=detail, data=request.data)
# 	if serializer.is_valid():
# 		serializer.save()
# 	return Response(serializer.data)

# #DELETE views for deleting an old Offer,Parameter or Detail

# @api_view(['GET','DELETE'])
# def deleteParameter(request, pk):
# 	parameter = Parameter.objects.get(id=pk)
# 	parameter.delete()
# 	return Response('Parameter succsesfully deleted!')

# @api_view(['GET','DELETE'])
# def deleteDetail(request, pk):
# 	detail = Detail.objects.get(id=pk)
# 	detail.delete()
# 	return Response('Detail succsesfully deleted!')