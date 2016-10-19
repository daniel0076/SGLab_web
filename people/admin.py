from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ch', 'identity', 'email', 'tel', 'ext')

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ch', 'email', 'tel', 'ext')

@admin.register(models.TeacherEducation)
class TeacherEducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_time')

@admin.register(models.TeacherExp)
class TeacherExpAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_time')

@admin.register(models.TeacherAwards)
class TeacherAwardsAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_time')

@admin.register(models.TeacherMember)
class TeacherMemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_time')

@admin.register(models.TeacherPublication)
class TeacherPublicationAdmin(admin.ModelAdmin):
    search_fields = ['title','category']
    list_display = ('title', 'category', 'upload_file')

