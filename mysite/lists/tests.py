from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .models import Item,List

from .views import home_page,new_list


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        expected_html = render_to_string('lists/home.html', request=request)
        self.assertEqual(response.content.decode(), expected_html)

    # def test_home_page_can_save_a_POST_request(self):
    #     request = HttpRequest()
    #     request.method = "POST"
    #     request.POST['item_text'] = 'A new list item'
    #
    #     response = home_page(request)
    #
    #     self.assertEqual(Item.objects.all().count(), 1)
    #     new_item = Item.objects.all()[0]
    #     self.assertEqual(new_item.text, 'A new list item')

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['item_text'] = 'A new list item'

        response = new_list(request)
        n_list = List.objects.first()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/%d/' %(n_list.id))

    # def test_home_page_only_saves_items_when_necessary(self):
    #     request = HttpRequest()
    #     home_page(request)
    #     self.assertEqual(Item.objects.count(), 0)


class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list_ = List.objects.create()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list,list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list,list_)


class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.all().count(), 1)
        new_item = Item.objects.all()[0]
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        n_list = List.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/lists/%d/' %(n_list.id,))

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/%d/' %(list_.id,))
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1',list=correct_list)
        Item.objects.create(text='itemey 2',list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='other list itemey 1',list=other_list)
        Item.objects.create(text='other list itemey 2',list=other_list)

        response = self.client.get('/lists/%d/' %(correct_list.id,))

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list itemey 1')
        self.assertNotContains(response, 'other list itemey 2')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' %(correct_list.id,))
        self.assertEqual(response.context['list'],correct_list)

class NewItemTest(TestCase):
    def test_can_save_a_POST_requests_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post('/lists/%d/add_item' %(correct_list.id,),data={'item_text':'A new item for an exiting list'})

        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'A new item for an exiting list')
        self.assertEqual(new_item.list,correct_list)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post('/lists/%d/add_item' %(correct_list.id,),data={'item_text':'A new item for an exiting list'})

        self.assertRedirects(response,'/lists/%d/' %(correct_list.id,))