from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
from courses.assessments.models import QuestionSet, StudentAnswerSet
from courses.models import Week


@login_required
def assessments_view(request, course_id):
    weeks = Week.objects.filter(course=course_id)
    return render(request, "courses/assessments/assessments.html", {"weeks": weeks})


def assessment_overview(request, course_id, week_id, assessment_id):
    questionset = StudentAnswerSet.objects.get(course=course_id, week=week_id, number=assessment_id)
    return render(request, "courses/assessments/assessment_overview.html", {"questionset": questionset})