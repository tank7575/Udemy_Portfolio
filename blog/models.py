from django.db import models
from django.utils import timezone



class Blog(models.Model):
    Title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')



