
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static 
from send_image_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')),
    path('',include('accounts.urls')),
    path('',include('videoset.urls')),
    path('',include('send_image_app.urls')),
    path('accounts/',include('django.contrib.auth.urls')),

]
