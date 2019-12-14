from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateField()
    body = models.TextField()

