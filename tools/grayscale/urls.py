from .views import *
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('takephoto/', takePhoto, name="takephoto"), # Standardized path to lowercase and added trailing slash
    path('', takePhoto, name="home"),
    path('compress/', compressing, name="compress"), # Added trailing slash
    path('resizing/', resizing, name="resizing"), # Added trailing slash
    path('rotatephoto/', rotate, name="rotatephoto"), # Standardized path to match name and added trailing slash
    path('signin/', signin, name="signin"), # Changed path to 'signin' for consistency
    path('crop/', Crop, name="crop"), # Added trailing slash
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)