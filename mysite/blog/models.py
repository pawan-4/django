from django.conf import settings
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField

class Category(models.Model):
    title = models.CharField(max_length=200,null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title',unique=True)
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title',unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
