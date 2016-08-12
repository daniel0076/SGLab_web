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
    name = models.CharField(u'Name', max_length=64)
    highest_edu = models.CharField(u'Highest Education', max_length=256)
    research_topic = models.TextField(u'Research Topic', blank=True)
    tel = models.CharField(u'Tel', max_length=32, blank=True)
    ext = models.CharField(u'Ext', max_length=10, blank=True)
    email = models.EmailField(u'Email', null=True, blank=True)
    photo = models.ImageField(u'Photo', upload_to='member_photos',
                              null=True, blank=True)
