from django.urls import path
from ga_course import views

app_name = 'ga_course'

urlpatterns = [
    path('', views.index, name='index'),
]
