from django.contrib import admin

from .models import Receipt, Comment, Profile

admin.site.register(Receipt)
admin.site.register(Comment)
admin.site.register(Profile)
