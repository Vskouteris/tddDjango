from django.urls import path
from backend import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.home_page,name='home'),
    path('new/',views.newOPD,name='new OPD'),
    
    path('offers/',views.OfferViewList.as_view(),name='offers list'),
    path('parameters/',views.ParameterViewList.as_view(),name='parameters list'),
    path('details/',views.DetailViewList.as_view(),name='details list'),

    path('offers/<int:pk>/', views.OfferRUD.as_view(), name="one offer"),
    path('parameters/<int:pk>/', views.ParameterRUD.as_view(), name="one parameter"),
    path('details/<int:pk>/', views.DetailRUD.as_view(), name="one detail"),

]

urlpatterns = format_suffix_patterns(urlpatterns)