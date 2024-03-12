# from unittest import skip
# from django.tests import LiveServerTestCase
# from selenium import webdriver
# from myapp.models import Task
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
#
# class NameFunctionalTest(LiveServerTestCase):
#     def setUp(self):
#         self.selenium = webdriver.Chrome()
#         super().setUp()
#
#     def tearDown(self):
#         self.selenium.quit()
#         super().tearDown()
#
#     def test_product_list_functional(self):
#         # Create tests data
#         Task.objects.create(name='Название услуги')
#         Task.objects.create(name='Фотостудия')
#
#         # Simulate user interactions using Selenium
#         self.selenium.get(self.live_server_url + '/Staff/')
#         self.assertIn('Список Товаров', self.selenium.title)
#         names = self.selenium.find_elements(By.TAG_NAME, 'td')
#         self.assertEqual(len(names), 2)
#         self.assertEqual(names[0].text, 'Название услуги')
#         self.assertEqual(names[1].text, 'Фотостудия')