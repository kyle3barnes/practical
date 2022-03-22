from django.http import HttpResponse
from django.shortcuts import render
from ga_course.models import Course

# Create your views here.


def index(request):
    course_list = Course.objects.all()
    context_dict = {'courses': course_list}

    return render(request, 'ga_course/index.html', context=context_dict)
