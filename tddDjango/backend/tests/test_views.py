from django.test import SimpleTestCase,TestCase,tag
from django.urls import reverse,resolve
from backend.views import home_page
from backend.models import Offer,Parameter,Detail
from backend.serializers import OfferSerializer,ParameterSerializer,DetailSerializer

# Here I want to test the logic in views AND I will start with the crud operations.For example I have to test that when I create an offer it gets saved in the database and I
# can make a get/put/delete request to this offer.  

@tag('views')
class TestViews(TestCase):      # HOW TO TEST JUST THIS CLASS??? by putting tags decorator and then  : python manage.py test --tag=views

    def setUp(self):
        self.offerList_url = reverse('offers list') 
        offer = Offer()
        

    def test_home_page_renders_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'backend/home.html')
    
    def test_OfferViewList_get_list(self):
        response = self.client.get(self.offerList_url)
        self.assertEquals(response.status_code,200)
        print(response.json())
