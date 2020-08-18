from cvbuilder.models import *
from django.test import TestCase
from django.urls import resolve
from cvbuilder.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):

        response = self.client.get('/cv/')

        self.assertTemplateUsed(response, 'template.html')

    def test_can_save_a_POST_request(self) :
        response = self.client.post('/cv/', data={'skill': 'A new skill'})
        self.assertEqual(SkillItem.objects.count(), 1)
        new_item = SkillItem.objects.first()
        self.assertEqual(new_item.text, 'A new skill')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],'/cv/')

    def test_can_save_a_second_POST_request(self) :
        response = self.client.post('/cv/', data={'personalprof' : 'A new profile'})
        self.assertEqual(PersonalProfileItem.objects.count(), 1)
        new_item = PersonalProfileItem.objects.last()
        self.assertEqual(new_item.text, 'A new profile')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

    def test_can_save_a_multivalue_POST_request(self) :
        response = self.client.post('/cv/', data={'placeofwork' : 'A new place of work', 'role' : 'A new role', 'startdatew':'A new start date', 'enddatew': 'A new enddate', 'description' : 'A new description', 'WorkSubmit':'Submit'})

        self.assertEqual(WorkExperience.objects.count(), 1)
        new_item = WorkExperience.objects.first()
        self.assertEqual(new_item.company, 'A new place of work')
        self.assertEqual(new_item.role, 'A new role')
        self.assertEqual(new_item.startdate, 'A new start date')
        self.assertEqual(new_item.enddate, 'A new enddate')
        self.assertEqual(new_item.description, 'A new description')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')


    def test_only_saves_items_when_necessary(self) :
        self.client.get('/cv/')
        self.assertEqual(SkillItem.objects.count(), 0)

    def test_displays_all_list_items(self) :
        SkillItem.objects.create(text='itemskill 1')
        SkillItem.objects.create(text='itemskill 2')
        WorkExperience.objects.create(company='new company 1', role='new role 1', startdate='new startdate1', enddate='new enddate1', description='new description1')
        WorkExperience.objects.create(company='new company 2', role='new role 2', startdate='new startdate2', enddate='new enddate2', description='new description2')

        response = self.client.get('/cv/')


        self.assertIn('itemskill 1', response.content.decode())
        self.assertIn('itemskill 2', response.content.decode())
        self.assertIn('new company 2', response.content.decode())
        self.assertIn('new role 2', response.content.decode())
        self.assertIn('new startdate2', response.content.decode())
        self.assertIn('new enddate2', response.content.decode())
        self.assertIn('new description2', response.content.decode())
        self.assertIn('new role 1', response.content.decode())
        self.assertIn('new company 1', response.content.decode())
        self.assertIn('new startdate1', response.content.decode())
        self.assertIn('new enddate1', response.content.decode())
        self.assertIn('new description2', response.content.decode())



class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = SkillItem()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = SkillItem()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = SkillItem.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


    def test_can_save_and_retrieve_mutliple_model_item(self):
        first_item = WorkExperience()
        first_item.company = 'First work title'
        first_item.role = 'First role title'
        first_item.startdate = 'First startdate'
        first_item.enddate='First enddate'
        first_item.description = 'First description'
        first_item.save()

        second_item = WorkExperience()
        second_item.company = 'Second work title'
        second_item.role = 'Second role title'
        second_item.startdate = 'Second startdate'
        second_item.enddate='Second enddate'
        second_item.description = 'Second description'
        second_item.save()



        saved_items = WorkExperience.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.company, 'First work title')
        self.assertEqual(first_saved_item.role, 'First role title')
        self.assertEqual(first_saved_item.startdate, 'First startdate')
        self.assertEqual(first_saved_item.enddate, 'First enddate')
        self.assertEqual(first_saved_item.description, 'First description')
        self.assertEqual(second_saved_item.company, 'Second work title')
        self.assertEqual(second_saved_item.role, 'Second role title')
        self.assertEqual(second_saved_item.startdate, 'Second startdate')
        self.assertEqual(second_saved_item.enddate, 'Second enddate')
        self.assertEqual(second_saved_item.description, 'Second description')
