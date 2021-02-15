from django.urls import path
from backend import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('testDatabase/',views.testDatabase,name='testDatabase'),
]