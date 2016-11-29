from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.ExternalLinks)
class ExternalLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'intro' )
