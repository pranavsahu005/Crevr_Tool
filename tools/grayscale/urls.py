from .views import *
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # The root URL '/' and '/grayscale/' will both point to the takePhoto view.
    path('', takePhoto, name="home"),
    path('grayscale/', takePhoto, name="takephoto"),
    path('compress/', compressing, name="compress"),
    path('resize/', resizing, name="resizing"),
    path('rotate/', rotate, name="rotatephoto"),
    path('signup',signup,name="signup")
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)