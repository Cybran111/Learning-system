from django.shortcuts import render, redirect
from courses.forms import NewCourseForm
from courses.models import Course

# Create your views here.

def home_page(request):

    return render(request, 'homepage.html', {"courses": Course.objects.all()})

def course_view(request, course_id):

    return render(request, 'course_page.html', {"course": Course.objects.get(pk=course_id)})

def create_course(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            new_course = Course()
            new_course.title = request.POST['title']
            new_course.short_description = request.POST['short_desc']
            new_course.full_description = request.POST['full_desc']
            new_course.save()
            return redirect('courses/%d' % (new_course.id,))
    else:
        form = NewCourseForm()

    return render(request, 'new_course.html', {"new_course_form": form})