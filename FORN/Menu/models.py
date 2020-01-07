from django.db import models


class Menu(models.Model):
    menu_title = models.CharField('Название меню', max_length=100)
    menu_desc = models.TextField('Описание меню')
    menu_cal = models.IntegerField('Калорийность')
