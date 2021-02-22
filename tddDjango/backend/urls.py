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

    path('create_offer/',views.create_offer,name='create_offer'),
    path('create_parameter/',views.create_parameter,name='create_parameter'),
    path('create_detail/',views.create_detail,name='create_detail'),

    path('update_offer/<int:pk>/',views.update_offer,name='update_offer'),
    path('update_parameter/<int:pk>/',views.update_parameter,name='update_parameter'),
    path('update_detail/<int:pk>/',views.update_detail,name='update_detail'),

    path('delete_offer/<int:pk>/',views.deleteOffer,name='delete_offer'),
    path('delete_parameter/<int:pk>/',views.deleteParameter,name='delete_parameter'),
    path('delete_detail/<int:pk>/',views.deleteDetail,name='delete_detail'),

]