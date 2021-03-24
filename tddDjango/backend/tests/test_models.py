from django.test import TestCase,tag
from model_bakery import baker

from backend.models import Offer,Parameter,Detail
# from backend.views import home_page
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

    #test that adding detail to a parameter + removing 

    def test_constractor_manytomany_add(self):      
        details = baker.make(Detail,_quantity=3)
        parameter = baker.make(Parameter)
        
        # test adding one parameter to one detail
        details[1].parameters.add(parameter)
        self.assertEquals(details[1].parameters.all().count(),1)
        self.assertEquals(parameter.details.all().count(),1)

        # test adding more details to one parameter
        parameter.details.add(details[0],details[1],details[2])
        self.assertEquals(parameter.details.all().count(),3)

    def test_constractor_manytomany_remove(self):      
        details_set = baker.make(Detail,_quantity=3)
        parameter = baker.make(Parameter, details=details_set)

        details_set[0].parameters.remove(parameter)
        #test that 3-1=2    (The detail was removed from the parameter so now the parameter haw only two details left)
        self.assertEquals(parameter.details.all().count(),2)
        #test that 1-1=0    (This detail was part of only one parameter and when we removed it from there it is not part of any parameter)
        self.assertEquals(details_set[0].parameters.all().count(),0)
        
@tag('parametermodel')
class TestParameterModel(TestCase):      # python manage.py test --tag=parametermodel

    def test_save_for_INvalid_parameter(self):
        Parameter.objects.create()
        first = Parameter.objects.first()
        self.assertIsNone(first)

    def test_save_for_valid_parameter(self):
        Parameter.objects.create(name='test Name')
        first = Parameter.objects.first()
        self.assertIsNotNone(first)

    def test__str__(self):
        Parameter.objects.create(name='test Name')
        first = Parameter.objects.first()
        self.assertEquals(str(first),"test Name-")

    #test that adding parameter to an offer + removing 

    def test_constractor_manytomany_add(self):      
        parameters = baker.make(Parameter,_quantity=3)
        offer = baker.make(Offer)
        
        # test adding one offer to one parameter
        parameters[1].offers.add(offer)
        self.assertEquals(parameters[1].offers.all().count(),1)
        self.assertEquals(offer.parameters.all().count(),1)

        # test adding more parameters to one offer
        offer.parameters.add(parameters[0],parameters[1],parameters[2])
        self.assertEquals(offer.parameters.all().count(),3)

    def test_constractor_manytomany_remove(self):      
        parameters_set = baker.make(Parameter,_quantity=3)
        offer = baker.make(Offer, parameters=parameters_set)

        parameters_set[0].offers.remove(offer)
        #test that 3-1=2    (The parameter was removed from the offer so now the offer haw only two parameters left)
        self.assertEquals(offer.parameters.all().count(),2)
        #test that 1-1=0    (This parameter was part of only one offer and when we removed it from there it is not part of any offer)
        self.assertEquals(parameters_set[0].offers.all().count(),0)

@tag('offermodel')
class TestOfferModel(TestCase):      # python manage.py test --tag=offermodel

    def test_save_for_INvalid_offer(self):
        Offer.objects.create()
        first = Offer.objects.first()
        self.assertIsNone(first)

    def test_save_for_valid_offer(self):
        Offer.objects.create(customer_name='test Name')
        first = Offer.objects.first()
        self.assertIsNotNone(first)

    def test__str__(self):
        Offer.objects.create(customer_name='test Name')
        first = Offer.objects.first()
        self.assertEquals(str(first),"test Name asked for None pieces")
