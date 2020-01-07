from django.contrib import admin

from .models import Video, VideoComment

admin.site.register(Video)
admin.site.register(VideoComment)
