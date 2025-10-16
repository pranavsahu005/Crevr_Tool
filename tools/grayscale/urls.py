from .views import *
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('grayscale/', process_image, name="grayscale"),
    path('compress/', process_image, name="compress"),
    path('resize/', process_image, name="resizing"),
    path('crop/', process_image, name="crop"),
    path('rotate/', process_image, name="rotate"),
    path('signin/', signup, name="signin"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)