from django.urls import path
from backend import views

urlpatterns = [
    path('',views.home_page,name='home'),
    
    path('get_list_of_offers/',views.get_list_of_offers,name='get_list_of_offers'),
    path('get_list_of_parameters/',views.get_list_of_parameters,name='get_list_of_parameters'),
    path('get_list_of_details/',views.get_list_of_details,name='get_list_of_details'),

    path('offer/<int:args>/', views.get_offer, name="get_offer"),
    path('parameter/<int:args>/', views.get_parameter, name="get_parameter"),
    path('detail/<int:args>/', views.get_detail, name="get_detail"),

]