from django.db import models
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    video_title = models.CharField('Название мастер класса', max_length=100)
    video_desc = models.TextField('Описание мастер класса')
    pub_date = models.DateTimeField('Дата публикации', auto_now=True)
    video_video = EmbedVideoField()

    def __str__(self):
        return self.video_title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class VideoComment(models.Model):
    comment_author = models.CharField('Имя автора', max_length=60)
    comment_text = models.TextField('Текст комментария')
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_author

    class Meta:
        verbose_name = 'Видео комментарий'
        verbose_name_plural = 'Видео комментарии'


