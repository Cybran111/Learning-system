from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
from courses.models import Week


@login_required
def assessments_view(request, course_id):
    weeks = Week.objects.filter(course=course_id)
    return render(request, "courses/assessments/assessments.html", {"weeks": weeks})