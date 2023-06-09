from django.db import models

"""Формирование БД с необходимыми полями"""
class Forecast(models.Model):
    name = models.CharField(max_length=12)
    data = models.DateField()
    description = models.TextField()
    lucky_number = models.PositiveIntegerField()
    color = models.TextField()

    def __str__(self):
        return f'Знак: {self.name} | Дата: {self.data}'
