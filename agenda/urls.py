from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path('', include('applications.home.urls')),
    re_path('', include('applications.person.urls')),
]