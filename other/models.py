from django.db import models

# Create your models here.

class ExternalLinks(models.Model):
    title= models.CharField(u'標題',max_length=128)
    url = models.CharField(u'連結',max_length=128, blank=True, null=True)
    intro = models.TextField(u'簡介', blank=True, null=True)

    class Meta:
        managed = True
        verbose_name = u"相關連結"
        verbose_name_plural = u"相關連結"

    def __str__(self):
        return 'Links: {}'.format(self.title)
