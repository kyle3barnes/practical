from django.contrib import admin
from django.urls import path, include
from ga_course import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/', include('ga_course.urls')),
    path('admin/', admin.site.urls),
]
