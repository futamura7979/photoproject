from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'videoset'

urlpatterns = [
    path('upload_video', views.upload_video, name='upload_video'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)