from django.test import TestCase,tag
# from django.urls import reverse,resolve
# from backend.views import home_page
from backend.models import Offer,Parameter,Detail
# from backend.serializers import OfferSerializer,ParameterSerializer,DetailSerializer

@tag('detailmodel')
class TestDetailModel(TestCase):      # HOW TO TEST JUST THIS CLASS??? by putting tags decorator and then  : python manage.py test --tag=detailmodel

    def test_save_for_INvalid_detail(self):
        Detail.objects.create()
        first = Detail.objects.first()
        self.assertIsNone(first)

    def test_save_for_valid_detail(self):
        Detail.objects.create(name='test Name')
        first = Detail.objects.first()
        self.assertIsNotNone(first)

    def test__str__(self):
        Detail.objects.create(name='test Name')
        first = Detail.objects.first()
        self.assertEquals(str(first),"test Name-('NO OPTION', 'NO OPTION')")

    def test_constractor_manytomany(self):      #test that adding detail to a parameter + removing + changing from one par to onother
        pass