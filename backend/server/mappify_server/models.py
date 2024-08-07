# models.py
# This file defines the Video model, which includes fields for the video title,
# upload date, and the video file itself. This model is used to store and manage
# information about the uploaded videos.
from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title

class Map(models.Model):
    place = models.CharField(max_length=255)
    date_of_upload = models.DateField()
    unique_photo_name = models.CharField(max_length=255, unique=True)

