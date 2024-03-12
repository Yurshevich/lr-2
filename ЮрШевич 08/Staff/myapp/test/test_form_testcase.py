from unittest import skip
from django.test import TestCase
from myapp.forms import TaskForm


class FormTest(TestCase):
    def test_form_valid(self):
        form_data = {'name': 'макияж', 'place':'Юбилейная 3','price':'1400','square':'13:00',}
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {'name': '','place': '', 'price': '', 'square': '',}
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())