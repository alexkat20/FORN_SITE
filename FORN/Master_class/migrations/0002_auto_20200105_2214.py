# Generated by Django 2.2.7 on 2020-01-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_class', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_video',
            field=models.FileField(upload_to='images/', verbose_name='Ссылка для видео'),
        ),
    ]