from django.test import TestCase
from myapp.models import Task


class CustomersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(name='Фото', place='100', price='758', square='5')

    def test_first_name_label(self):
        models = Task.objects.get(id=1)
        field_label = models._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название услуги')

    def test_phone_label(self):
        models = Task.objects.get(id=1)
        field_label = models._meta.get_field('place').verbose_name
        self.assertEquals(field_label, 'Объём')

    def test_surname_max_length(self):
        models = Task.objects.get(id=1)
        max_length = models._meta.get_field('price').max_length
        self.assertEquals(max_length, 10)

    def test_get_absolute_url(self):
        models = Task.objects.get(id=1)
        self.assertEquals(models.get_absolute_url(), '/task/1/')
