from unittest import skip
from django.tests import TestCase
from models import Task


class MyModelTest(TestCase):
    def setUp(self):
        self.object = Task.objects.create(name="Фотостудия")

    def test_str_representation(self):
        self.assertEqual(str(self.object), 'Фотостудия')

    def tearDown(self):
        pass