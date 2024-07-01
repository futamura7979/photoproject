from django.db import models

class ModelFile(models.Model):
    image = models.ImageField(upload_to='documents/')

class VideoContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    upload_date = models.DateTimeField()
    original_name = models.CharField(max_length=200)
    filename = models.CharField(max_length=200, default="")
    thumb_frame = models.IntegerField(default=0)