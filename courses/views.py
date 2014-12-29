from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from courses.forms import NewCourseForm
from courses.models import Course, Week, Lecture


# Create your views here.

def home_page(request):
    return render(request, 'homepage.html', {"courses": Course.objects.all()})

def course_view(request, course_id):
    return render(request, 'course_page.html', {"course": Course.objects.get(pk=course_id)})

def lectures_view(request, course_id):
    course = Course.objects.get(pk=course_id)
    lectures = (Lecture.objects.filter(week=week)
                for week in Week.objects.filter(course=course)
    )

    return render(request, 'lectures.html', {'lectures_by_week': lectures})




def create_course_view(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            new_course = Course()
            new_course.title = request.POST['title']
            new_course.short_description = request.POST['short_desc']
            new_course.full_description = request.POST['full_desc']
            new_course.save()
            return redirect(reverse('courses:course_page', args=(new_course.id,)))
    else:
        form = NewCourseForm()

    return render(request, 'new_course.html', {"new_course_form": form})
