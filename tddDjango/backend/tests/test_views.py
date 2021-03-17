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
        offer = Offer.objects.create(customer_name='test customer')

    def test_get_correct_offer(self):
        #find by id the offer i want and not some other offer
        pass
 
    def test_get_correct_parameters_for_this_offer(self):
        pass

    def test_update_this_offer(self):
        pass
