from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ch', 'identity', 'email', 'tel', 'ext')
