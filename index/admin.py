from django.contrib import admin
from . import models
admin.AdminSite.site_header="Space Geodecy Lab 管理後台"
admin.AdminSite.site_title="Space Geodecy Lab"

# Register your models here.

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time','updated_time')
