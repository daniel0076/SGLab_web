from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ch', 'identity', 'email', 'tel', 'ext')

@admin.register(models.Teacher)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ch', 'email', 'tel', 'ext')

@admin.register(models.TeacherEducation)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_time')

@admin.register(models.TeacherExp)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_time')

@admin.register(models.TeacherAwards)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_time')

@admin.register(models.TeacherMember)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_time')

@admin.register(models.TeacherPublication)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_file')

