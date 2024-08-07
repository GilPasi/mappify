# forms.py
# This file defines the form used to upload videos. The VideoForm class is a
# ModelForm that includes fields for the video title and the video file.
from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']
