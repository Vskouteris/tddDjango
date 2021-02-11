from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from backend.views import *

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

    def test_home_page_view_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>') or html.startswith('<!DOCTYPE html>') ,msg = f"html starts with : {html[:10]}")
        self.assertIn('<title>Home Page</title>',html,msg=f"THE TTITLT INSIDE HTML IS DIFFERENT from THE ASSERT TEST")
        self.assertTrue(html.endswith('</html>'),msg = f"html ends with : {html[-10:]}")