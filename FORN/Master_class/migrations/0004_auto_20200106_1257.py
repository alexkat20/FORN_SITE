# Generated by Django 2.2.7 on 2020-01-06 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_class', '0003_auto_20200105_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_desc',
            field=models.TextField(verbose_name='Описание мастер класса'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_title',
            field=models.CharField(max_length=100, verbose_name='Название мастер класса'),
        ),
    ]