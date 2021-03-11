from django.urls import path
from backend import views

urlpatterns = [
    path('',views.home_page,name='home'),
    
    path('get_list_of_offers/',views.OfferViewList.as_view(),name='offers list'),
    path('get_list_of_parameters/',views.ParameterViewList.as_view(),name='parameters list'),
    path('get_list_of_details/',views.DetailViewList.as_view(),name='details list'),

    path('create_offer/',views.OfferViewList.as_view(),name='add offer'),
    path('create_parameter/',views.ParameterViewList.as_view(),name='add parameter'),
    path('create_detail/',views.DetailViewList.as_view(),name='add detail'),
     
    path('offer/<int:args>/', views.OfferRUD.as_view(), name="get_offer"),
    path('parameter/<int:args>/', views.ParameterRUD.as_view(), name="get_parameter"),
    path('detail/<int:args>/', views.DetailRUD.as_view(), name="get_detail"),

    path('update_offer/<int:pk>/',views.OfferRUD.as_view(),name='update_offer'),
    path('update_parameter/<int:pk>/',views.ParameterRUD.as_view(),name='update_parameter'),
    path('update_detail/<int:pk>/', views.DetailRUD.as_view(),name='update_detail'),

    path('delete_offer/<int:pk>/',views.OfferRUD.as_view(),name='delete_offer'),
    path('delete_parameter/<int:pk>/',views.ParameterRUD.as_view(),name='delete_parameter'),
    path('delete_detail/<int:pk>/', views.DetailRUD.as_view(),name='delete_detail'),

]