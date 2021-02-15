from django.urls import path
from backend import views

urlpatterns = [
    path('',views.home_page,name='home'),
    
    path('get_offers/',views.get_offers,name='get_offers'),
    path('get_parameters/',views.get_parameters,name='get_parameters'),
    path('get_details/',views.get_details,name='get_details'),

]