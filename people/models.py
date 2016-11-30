from django.db import models

# Create your models here.


class Member(models.Model):
    IDENTITY = (
        ('Postdoc', 'Postdoc'), ('PhD Student', 'PhD Student'),
        ('Master Student', 'Master Student'),
        ('Assistant', 'Assistant'),
    )
    id = models.AutoField(primary_key=True)
    identity = models.CharField(u'Identity', max_length=32, choices=IDENTITY)
    name_en = models.CharField(u'Name(EN)', max_length=64)
    name_ch = models.CharField(u'Name(中文)', max_length=64)
    highest_edu_en = models.CharField(u'Highest Education(EN)', max_length=256, blank=True)
    highest_edu_ch = models.CharField(u'最高學歷(中文)', max_length=256, blank=True)
    research_topic = models.TextField(u'Research Topic', blank=True)
    tel = models.CharField(u'Tel', max_length=32, blank=True)
    ext = models.CharField(u'Ext', max_length=10, blank=True)
    email = models.EmailField(u'Email', null=True, blank=True)
    photo = models.ImageField(u'Photo', upload_to='member_photos',
                              null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = u"實驗室成員"
        verbose_name_plural = u"實驗室成員"

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name_en = models.CharField(u'Name(EN)', max_length=64)
    name_ch = models.CharField(u'Name(中文)', max_length=64)
    research_topic = models.TextField(u'Research Topic', blank=True)
    tel = models.CharField(u'Tel', max_length=32, blank=True)
    ext = models.CharField(u'Ext', max_length=10, blank=True)
    email = models.EmailField(u'Email', null=True, blank=True)
    photo = models.ImageField(u'Photo', upload_to='member_photos',
                              null=True, blank=True)
    class Meta:
        managed = True
        verbose_name = u"指導教授"
        verbose_name_plural = u"指導教授"


class TeacherEducation(models.Model):
    title = models.TextField(u'學歷標題')
    update_time = models.DateTimeField(u'更新時間', auto_now=True)
    order = models.IntegerField(u'排序', help_text="大的在前", default = 1)

    class Meta:
        managed = True
        verbose_name = u"教授學歷"
        verbose_name_plural = u"教授學歷"


class TeacherExp(models.Model):
    title = models.TextField(u'學術經驗')
    update_time = models.DateTimeField(u'更新時間', auto_now=True)
    order = models.IntegerField(u'排序', help_text="大的在前", default = 1)
    class Meta:
        managed = True
        verbose_name = u"教授學術經驗"
        verbose_name_plural = u"教授學術經驗"

class TeacherAwards(models.Model):
    title = models.TextField(u'榮譽與成就')
    update_time = models.DateTimeField(u'更新時間', auto_now=True)
    order = models.IntegerField(u'排序', help_text="大的在前", default = 1)
    class Meta:
        managed = True
        verbose_name = u"教授榮譽與成就"
        verbose_name_plural = u"教授榮譽與成就"

class TeacherMember(models.Model):
    title = models.TextField(u'成員')
    update_time = models.DateTimeField(u'更新時間', auto_now=True)
    order = models.IntegerField(u'排序', help_text="大的在前", default = 1)
    class Meta:
        managed = True
        verbose_name = u"教授職位"
        verbose_name_plural = u"教授職位"

class TeacherPublication(models.Model):
    CATEGORY = (
            ('journal_paper', 'journal_paper'),
            ('conf_paper', 'conf_paper'),
            ('book_chapter', 'book_chapter'),
            )
    title = models.TextField(u'標題')
    category = models.CharField(u'類型', max_length=32, choices=CATEGORY)
    date = models.DateTimeField(u'日期')
    upload_file = models.FileField(u'論文PDF上傳',
                                   upload_to='publications', null=True, blank=True)
    update_time = models.DateTimeField(u'更新時間', auto_now=True)

    class Meta:
        managed = True
        verbose_name = u"論文"
        verbose_name_plural = u"論文"
