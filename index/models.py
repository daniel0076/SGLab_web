from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(u'標題', max_length=100)
    content = RichTextUploadingField(u'內容')
    created_time = models.DateTimeField(u'發佈時間', auto_now_add=True)
    updated_time = models.DateTimeField(u'更新時間', auto_now=True)

    class Meta:
        verbose_name = "公告系統"
        verbose_name_plural = "公告系統"
