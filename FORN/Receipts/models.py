from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Receipt(models.Model):
    receipt_title = models.CharField('Название рецепта', max_length=100)
    receipt_text = models.TextField('Текст рецепта')
    pub_date = models.DateTimeField('Дата публикации', auto_now=True)
    author_name = models.CharField('Имя автора', max_length=100, null=True, blank=True)
    receipt_calories = models.IntegerField('Калорийность блюда')
    receipt_products = models.TextField('Продукты')
    receipt_kitchen = models.CharField('Кухня', max_length=100)
    receipt_img = models.ImageField('Фото', null=True, blank=True, upload_to='images')

    def __str__(self):
        return self.receipt_title



    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Comment(models.Model):
    comment_author = models.CharField('Имя автора', max_length=60)
    comment_text = models.TextField('Текст комментария')
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True, default=0)
    menu = models.ForeignKey('Menu.Menu', blank=True, null=True, on_delete=models.SET_NULL)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()