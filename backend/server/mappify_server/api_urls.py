from django.urls import path
from .api_views import UploadVideoAPIView,ImageView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('get-csrf-token/', UploadVideoAPIView.as_view(), name='request-csrf-token'),
    path('upload/', UploadVideoAPIView.as_view(), name='upload-video'),
    path('media/maps/<str:image_name>/', ImageView.as_view(), name='get-image'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

