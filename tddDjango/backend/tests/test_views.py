from django.test import SimpleTestCase,TestCase,tag
from django.urls import reverse,resolve
from backend.views import home_page
from backend.models import Offer,Parameter,Detail
from backend.serializers import OfferSerializer,ParameterSerializer,DetailSerializer

# Here I want to test the logic in views AND I will start with the crud operations.For example I have to test that when I create an offer it gets saved in the database and I
# can make a get/put/delete request to this offer.  

@tag('views')
class TestViews(TestCase):      # HOW TO TEST JUST THIS CLASS??? by putting tags decorator and then  : python manage.py test --tag=views
      
    def test_home_page_renders_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'backend/home.html')

@tag('offerviewlist')
class TestOfferViewList(TestCase):

    def test_get_list_of_offers(self):
        offer1 = Offer.objects.create(customer_name='test customer')  
        offer2 = Offer.objects.create(customer_name='test customer 2') 
        response = self.client.get('/offers/')
        self.assertEquals(response.status_code,200)
        self.assertEquals(len(response.json()),2)
        

    def test_post_new_valid_offer(self):
        response = self.client.post('/offers/',data={   'customer_name' : 'testcustomer' ,
                                                        'description' :  "test saving to db with post"})
        self.assertEqual(Offer.objects.count(), 1)
        new_offer = Offer.objects.first()
        self.assertEqual(new_offer.description, 'test saving to db with post')

    # def test_post_new_INvalid_offer(self):
    #     pass

@tag('parameterviewlist')
class TestParameterViewList(TestCase):

    def test_get_list_of_parameters(self):
        parameter1 = Parameter.objects.create(name="test parameter 1")  
        parameter2 = Parameter.objects.create(name='test parameter 2') 
        response = self.client.get('/parameters/')
        self.assertEquals(response.status_code,200)
        self.assertEquals(len(response.json()),2)
        

    def test_post_new_valid_parameter(self):
        response = self.client.post('/parameters/',data={'name' : 'testparameter' ,
                                                         'description' :  "test saving to db with post"})
        self.assertEqual(Parameter.objects.count(), 1)
        new_parameter = Parameter.objects.first()
        self.assertEqual(new_parameter.description, 'test saving to db with post')

    # def test_post_new_INvalid_parameter(self):
    #     pass

@tag('detailviewlist')
class TestDetailViewList(TestCase):

    def test_get_list_of_details(self):
        detail1 = Detail.objects.create(name="test detail 1")  
        detail2 = Detail.objects.create(name='test detail 2') 
        response = self.client.get('/details/')
        self.assertEquals(response.status_code,200)
        self.assertEquals(len(response.json()),2)
        

    def test_post_new_valid_detail(self):
        response = self.client.post('/details/',data={  'name' : 'testdetail' ,
                                                        'description' :  "test saving to db with post"})
        self.assertEqual(Detail.objects.count(), 1)
        new_detail = Detail.objects.first()
        self.assertEqual(new_detail.name, 'testdetail')


    # def test_post_new_INvalid_detail(self):
    #     pass

@tag('offerrud')
class TestOfferRUD(TestCase):
    def setUp(self):
        #   ATTENTION I have to create an offer with all fields valid and linked parameters.so i have to also create some parameters before the offer 
    
        par1 =Parameter.objects.create(name='test parameter1',extra_price=0,description='parameter for testing offers')
        par2 =Parameter.objects.create(name='test parameter2',extra_price=0,description='parameter for testing offers')
        Offer.objects.create(customer_name='test offer',extra_price=0,description='testing yo man',number=250)
        Offer.objects.first().parameters.add(par1,par2)

    def test_get_correct_offer(self):
        offer = Offer.objects.first()   
        self.assertEquals(self.client.get(f'/offers/{offer.pk}/').json()['description'],'testing yo man')
 
    def test_get_correct_parameters_for_this_offer(self):
        offer = Offer.objects.first()

        offer_parameters =self.client.get(f'/offers/{offer.pk}/').json()['parameters']
        offer_parameters = list(map(int, offer_parameters))
        
        self.assertEquals(Parameter.objects.filter(id__in=offer_parameters).count(),2)

    def test_update_this_offer(self):
        offer = Offer.objects.first()

        response = self.client.put(f'/offers/{offer.pk}/',data={'description':'UPDATE YO MAN'},content_type='application/json')
        self.assertEquals(response.json()['description'],'UPDATE YO MAN')
        
    def test_delete_this_offer(self):
        offer = Offer.objects.first()
        
        self.client.delete(f'/offers/{offer.pk}/')
        self.assertEquals(len(Offer.objects.all()),0)
        

@tag('parameterrud')
class TestParameterRUD(TestCase):
    def setUp(self):
        #   ATTENTION I have to create an parameter with all fields valid and linked details.so i have to also create some details before the parameter 
        
        det1 =Detail.objects.create(name='test detail1',extra_price=0)
        det2 =Detail.objects.create(name='test detail2',extra_price=0)
        Parameter.objects.create(name='test parameter',extra_price=0,description='parameter created for testing')
        Parameter.objects.first().details.add(det1,det2)

    def test_get_correct_parameter(self):
        parameter = Parameter.objects.first()   
        self.assertEquals(self.client.get(f'/parameters/{parameter.pk}/').json()['description'],'parameter created for testing')
 
    def test_get_correct_details_for_this_parameter(self):
        parameter = Parameter.objects.first()

        parameter_details =self.client.get(f'/parameters/{parameter.pk}/').json()['details']
        parameter_details = list(map(int, parameter_details))
        # print(parameter_details)  #here I  should print the  details for this parameter
        self.assertEquals(Detail.objects.filter(id__in=parameter_details).count(),2)

    def test_update_this_parameter(self):
        parameter = Parameter.objects.first()

        response = self.client.put(f'/parameters/{parameter.pk}/',data={'description':'UPDATE YO MAN'},content_type='application/json') #here should self.assert that new description != of old description
        self.assertEquals(response.json()['description'],'UPDATE YO MAN')
        
    def test_delete_this_parameter(self):
        parameter = Parameter.objects.first()
        
        self.client.delete(f'/parameters/{parameter.pk}/')
        self.assertEquals(len(Offer.objects.all()),0)