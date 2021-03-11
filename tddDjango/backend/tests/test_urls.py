from django.test import SimpleTestCase
from django.urls import reverse,resolve
from backend.views import *

class TestUrls(SimpleTestCase):
    
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func,home_page)

    def test_list_of_offers_is_resolved(self):
        url = reverse('offers list')
        self.assertEquals(resolve(url).func.view_class,OfferViewList)
    
    def test_list_of_parameters_is_resolved(self):
        url = reverse('parameters list')
        self.assertEquals(resolve(url).func.view_class,ParameterViewList)
    
    def test_list_of_details_is_resolved(self):
        url = reverse('details list')
        self.assertEquals(resolve(url).func.view_class,DetailViewList)

    # def test_home_url_is_resolved(self):
    #     url = reverse('home')
    #     self.assertEquals(resolve(url).func,home_page)

    # def test_home_url_is_resolved(self):
    #     url = reverse('home')
    #     self.assertEquals(resolve(url).func,home_page)

    # def test_home_url_is_resolved(self):
    #     url = reverse('home')
    #     self.assertEquals(resolve(url).func,home_page)
        
    # def test_home_url_is_resolved(self):
    #     url = reverse('home')
    #     self.assertEquals(resolve(url).func,home_page)











# from django.test import TestCase
# from django.urls import resolve
# from backend.views import *

# # Create your tests here.
# class HomePageTest(TestCase):
#     def test_root_url_resolves_to_home_page_view(self):
#         found = resolve('/')
#         self.assertEqual(found.func,home_page)

#     def test_home_page_view_return_correct_html(self):
#         response = self.client.get('/')
#         html = response.content.decode('utf-8')
#         self.assertTrue(html.startswith('<html>') or html.startswith('<!DOCTYPE html>') ,msg = f"html starts with : {html[:10]}")
#         self.assertIn('<title>Home Page</title>',html,msg=f"THE TITTLE INSIDE HTML IS DIFFERENT from THE ASSERT TEST")
#         self.assertTrue(html.endswith('</html>'),msg = f"html ends with : {html[-10:]}")
    
#     def test_home_template_is_the_template_used(self):
#         response = self.client.get('/')

#         self.assertTemplateUsed(response,'backend/home.html')