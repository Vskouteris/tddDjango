from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
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
	return render(request, 'backend/new_offer.html',context)


class OfferViewList(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					generics.GenericAPIView):

	queryset= Offer.objects.all()
	serializer_class=OfferSerializer
	renderer_classes = [TemplateHTMLRenderer]
	template_name='backend/new_offer.html'
	
	def get(self,request, *args, **kwargs):
		query = self.request.GET.get('search')
		if query:
			result=Offer.objects.filter(customer_name__contains=query)
		else:
			result = self.get_queryset()
		return Response({'offers': result})
		# return self.list(request, *args, **kwargs)

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
