from django.db import models

# Create your models here.


class Member(models.Model):
    IDENTITY = (
        ('Postdoc', 'Postdoc'),
        ('PhD Student', 'PhD Student'),
        ('Master Student', 'Master Student'),
        ('Assistant', 'Assistant'),
    )
    id = models.AutoField(primary_key=True)
    identity = models.CharField(u'Identity', max_length=32, choices=IDENTITY)
    name_en = models.CharField(u'Name(EN)', max_length=64)
    name_ch = models.CharField(u'Name(中文)', max_length=64)
    highest_edu_en = models.CharField(u'Highest Education(EN)', max_length=256)
    highest_edu_ch = models.CharField(u'最高學歷(中文)', max_length=256)
    research_topic = models.TextField(u'Research Topic', blank=True)
    tel = models.CharField(u'Tel', max_length=32, blank=True)
    ext = models.CharField(u'Ext', max_length=10, blank=True)
    email = models.EmailField(u'Email', null=True, blank=True)
    photo = models.ImageField(u'Photo', upload_to='member_photos',
                              null=True, blank=True)
