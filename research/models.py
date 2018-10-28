from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Research(models.Model):

    STYLE = (
        ('style1','藍色'),
        ('style2','粉色'),
        ('style3','米黃'),
    )

    id = models.AutoField(primary_key=True)
    title = models.TextField(u'Research_Title')
    sidebar_text = models.TextField(u'側邊欄文字')
    content = RichTextUploadingField(u'內容')
    order = models.IntegerField(u'排版順序', help_text=u'希望出現在第幾塊區域')
    style = models.CharField(u'背景樣式', max_length=10, choices = STYLE, default = "style1")
    created_time = models.DateTimeField(u'發佈時間', auto_now_add=True)
    updated_time = models.DateTimeField(u'更新時間', auto_now=True)

    class Meta:
        managed = True
        verbose_name = u"研究"
        verbose_name_plural = u"研究"
