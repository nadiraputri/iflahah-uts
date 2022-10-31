from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.bisa),
    path('belajar/', include('belajar.urls')),
    path('ipe/', include('ipe.urls')),
    path('iflahah/', include('iflahah.urls')),
]
