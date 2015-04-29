from django.shortcuts import render

# Create your views here.
from courses.models import Week


def assignments_view(request, course_id):
    weeks = Week.objects.filter(course=course_id)

    return render(request, "courses/assignments/assignments.html", {'weeks': weeks})