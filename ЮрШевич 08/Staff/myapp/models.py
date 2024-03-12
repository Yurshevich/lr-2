from django.db import models

class Task(models.Model):
    name = models.CharField('Название услуги', max_length=100)
    place = models.CharField('Имя сотрудника', max_length=100, )
    price = models.IntegerField('Цена')
    square = models.IntegerField('Время работы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотограф'
        verbose_name_plural = 'Фотографы'

