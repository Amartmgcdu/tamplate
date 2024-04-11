from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('about/', views.about_page, name='about'),
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
