from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Research)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sidebar_text', 'order', 'created_time', 'updated_time')
