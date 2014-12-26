from django.shortcuts import render
from course.models import Course

# Create your views here.

def home_page(request):
    return render(request, 'homepage.html', {"courses": Course.objects.all()})