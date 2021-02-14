from django.shortcuts import render
from .models import *

# Create your views here.
def home_page(request):
    offers = Offer.objects.all()
    parameters = Parameter.objects.all()
    details = Detail.objects.all()
    context = {'offers':offers, 'parameters':parameters, 'details':details}
    return render(request, 'backend/home.html',context)