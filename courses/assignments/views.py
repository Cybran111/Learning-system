from django.shortcuts import render

# Create your views here.
from courses.models import Course, Week


def assignments_view(request, course_id):

    course = Course.objects.get(pk=course_id)
    weeks = Week.objects.filter(course=course)

    return render(request, "courses/assignments/assignments.html", {"course_id": course.id, 'weeks': weeks})