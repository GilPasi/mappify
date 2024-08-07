from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'upload_date', 'video_file']

class GyroscopeDataSerializer(serializers.Serializer):
    x = serializers.FloatField()
    y = serializers.FloatField()
    z = serializers.FloatField()

class VideoUploadSerializer(serializers.Serializer):
    video = serializers.FileField()
    # gyroscopeData = serializers.ListField(
    #     child=GyroscopeDataSerializer()
    # )
