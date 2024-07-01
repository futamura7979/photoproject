from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'send_image_app'

urlpatterns = [
    path('predict/', views.predict_image, name='predict_image'),  
    path('image_upload', views.image_upload, name='image_upload'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)