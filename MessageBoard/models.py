from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse

class Post(models.Model):
  author= models.CharField(max_length=255)
  post_date = models.DateTimeField(auto_now_add=True)
  body=models.TextField()
  

  def __str__(self):
    return self.body + '|' +str(self.author )+ '|' +datetime(self.post_date)

  def get_absolute_url(self):
    return reverse('article-detail', args=(str(self.id)))


