from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)#标题
    slug = models.CharField(max_length=200)#网址
    body = models.TextField()#内容
    pub_date = models.DateTimeField(default=timezone.now)#发表时间
    #指定文章显示顺序是以pub_date为依据
    class Meta:
        ordering = ('-pub_date',)

    #文章标题为显示内容
    def __unicode__(self):
        return self.title