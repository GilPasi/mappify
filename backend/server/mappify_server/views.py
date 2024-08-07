# views.py
# This file defines the views for the mappify_server app. It includes views to
# upload videos, list all videos, view the details of a single video, and
# delete a video. Each view handles specific HTTP requests and renders the
# appropriate templates.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VideoForm
from .models import Video


def upload_video(request):
    print("Entering upload_video view")
    if request.method == 'POST':
        print('request is: ', request)
        print('POST is: ', request.POST)
        print('FILES is: ', request.FILES)

        print("Processing POST request in upload_video view")
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            print(f"Uploaded Video: {video.title} (ID: {video.pk})")
            return redirect('video_list')
        else:
            print("Form is not valid")
    else:
        print("Processing GET request in upload_video view")
        form = VideoForm()
    print("Rendering upload_video template")
    return render(request, 'mappify_server/upload_video.html', {'form': form})

def video_list(request):
    print("Entering video_list view")
    videos = Video.objects.all()
    print(f"Retrieved {videos.count()} videos from database")
    print("Rendering video_list template")
    return render(request, 'mappify_server/video_list.html', {'videos': videos})

def video_detail(request, pk):
    print(f"Entering video_detail view with pk: {pk}")
    video = get_object_or_404(Video, pk=pk)
    print(f"Viewed Video: {video.title} (ID: {video.pk})")
    print("Rendering video_detail template")
    return render(request, 'mappify_server/video_detail.html', {'video': video})

def delete_video(request, pk):
    print(f"Entering delete_video view with pk: {pk}")
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        print(f"Processing POST request in delete_video view for Video: {video.title} (ID: {video.pk})")
        video.delete()
        print(f"Deleted Video: {video.title} (ID: {video.pk})")
        return redirect('video_list')
    print("Rendering delete_video template")
    return render(request, 'mappify_server/delete_video.html', {'video': video})