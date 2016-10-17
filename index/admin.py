from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time','updated_time')
