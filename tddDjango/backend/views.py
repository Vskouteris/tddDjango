from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import mixins,status
from rest_framework import generics



# Create your views here.

def newOPD(request):
	formDetail = DetailSerializer()
	formParameter = ParameterSerializer()
	formOffer = OfferSerializer()
	style = {'template_pack': 'rest_framework/horizontal'}	#you need to send this style dict in your response in order to render_field

	context = {"formOffer":formOffer, "formParameter": formParameter, "formDetail":formDetail,
				"style" :style
	}
	return render(request, 'backend/new_OPD.html',context)


class OfferViewList(mixins.ListModelMixin,
					generics.GenericAPIView):

	queryset= Offer.objects.all()
	serializer_class=OfferSerializer
	renderer_classes = [TemplateHTMLRenderer]
	template_name='backend/offers_list.html'
	render_field_style = {'template_pack': 'rest_framework/vertical'}
	
	def get(self,request, *args, **kwargs):
		query = self.request.GET.get('search')
		if query:
			result=Offer.objects.filter(customer_name__contains=query)
		else:
			result = Offer.objects.all()
		return Response({'offers': result,'details': Detail.objects.all(),'parameters':Parameter.objects.all(),
							"formOffer":self.serializer_class(),"style":self.render_field_style})

	def post(self, request, *args, **kwargs):
		formOffer = OfferSerializer(data=request.data)
		if formOffer.is_valid():
			formOffer.save()
		else:
			# here should pop up a message that the offer is not saved
			pass 
		return Response({'offers': Offer.objects.all(),'details': Detail.objects.all(),'parameters':Parameter.objects.all(),
							"formOffer":self.serializer_class(),"style":self.render_field_style})

class ParameterViewList(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					generics.GenericAPIView):

	queryset= Parameter.objects.all()
	serializer_class=ParameterSerializer
	renderer_classes = [TemplateHTMLRenderer]
	template_name='backend/parameters_list.html'

	def get(self,request, *args, **kwargs):
		query = self.request.GET.get('search')
		if query:
			result=Parameter.objects.filter(name__contains=query)
		else:
			result = Parameter.objects.all()
		return Response({'parameters': result,'offers': Offer.objects.all(),'details': Detail.objects.all()})

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class DetailViewList(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					generics.GenericAPIView):

	queryset= Detail.objects.all()
	serializer_class=DetailSerializer
	renderer_classes = [TemplateHTMLRenderer]
	template_name='backend/details_list.html'

	def get(self,request, *args, **kwargs):
		query = self.request.GET.get('search')
		if query:
			result=Detail.objects.filter(name__contains=query)
		else:
			result = Detail.objects.all()
		return Response({'parameters':Parameter.objects.all(),'offers': Offer.objects.all(),'details': result})

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)		

#Offer get update delete
class OfferRUD(generics.RetrieveUpdateDestroyAPIView):
	queryset=Offer.objects.all()
	serializer_class= OfferSerializer
	renderer_classes = [TemplateHTMLRenderer]
	template_name='backend/new_OPD.html'

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		return Response({"offer":serializer.data,"formOffer":self.serializer_class()})

#Parameter get update delete
class ParameterRUD(generics.RetrieveUpdateDestroyAPIView):
	queryset=Parameter.objects.all()
	serializer_class= ParameterSerializer

#Detail get update delete
class DetailRUD(generics.RetrieveUpdateDestroyAPIView):
	queryset=Detail.objects.all()
	serializer_class= DetailSerializer
