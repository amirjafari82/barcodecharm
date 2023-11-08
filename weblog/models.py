from django.db import models
from django_jalali.db import models as jmodels

class Article(models.Model):
    image = models.ImageField(upload_to='static/images/articles')
    title = models.CharField(max_length=100)
    slug = models.SlugField(auto_created=True,unique=True,allow_unicode=True)
    views = models.IntegerField(default=0)
    created = jmodels.jDateTimeField(auto_now_add=True)
    text = models.TextField()