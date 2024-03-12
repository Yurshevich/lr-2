from django.test import TestCase
from .models import Task


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(name='Услуга', place='Цена', price=100, square=5)

    def test_name_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название услуги')

    def test_place_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('place').verbose_name
        self.assertEquals(field_label, 'Цена')

    def test_square_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('square').verbose_name
        self.assertEquals(field_label, 'Количество')
