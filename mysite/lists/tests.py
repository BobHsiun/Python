from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        print(found.func,home_page)
        self.assertEqual(found.func,home_page)

    # def test_home_page_return_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     self.assertTrue(response.content.startswith(b'<html>'))
    #     self.assertIn(b'<title>To-Do lists</title>',response.content)
    #     self.assertTrue(response.content.endswith(b'</html>'))

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        expected_html = render_to_string('lists/home.html',request=request)
        print(response.content.decode(),response)
        print(expected_html)
        self.assertEqual(response.content.decode(),expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
