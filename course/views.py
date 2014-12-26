from django.shortcuts import render
from course.models import Course

# Create your views here.

def home_page(request):

    return render(request, 'homepage.html', {"courses": Course.objects.all()})

def course_view(request, course_id):

    return render(request, 'course_page.html', {"course": Course.objects.get(pk=course_id)})