from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
from courses.assessments.forms import QuestionForm
from courses.assessments.models import QuestionSet, StudentAnswerSet
from courses.models import Week


@login_required
def assessments_view(request, course_id):
    weeks = Week.objects.filter(course=course_id)
    return render(request, "courses/assessments/assessments.html", {"weeks": weeks})


@login_required
def assessment_overview(request, course_id, week_id, assessment_id):
    questionset = QuestionSet.objects.get(course=course_id, week=week_id, number=assessment_id)
    feedbacks = StudentAnswerSet.objects.filter(user=request.user.id, questionset=assessment_id)
    return render(request, "courses/assessments/assessment_overview.html",
                  {"questionset": questionset, "feedbacks": feedbacks})


@login_required
def assessment_attempt(request, course_id, week_id, assessment_id):
    questionset = QuestionSet.objects.get(course=course_id, week=week_id, number=assessment_id)
    forms = tuple(QuestionForm(answers=tuple(answer for answer in question.possibleanswer_set.all()))
                  for question in questionset.question_set.all())

    questionset = (questionset.title, questionset.description, tuple(
        (
            question.text,
            QuestionForm(answers=tuple(answer for answer in question.possibleanswer_set.all()))
        )
        for question in questionset.question_set.all()
    ))
    # print questionset
    # return render(request, "courses/assessments/assessment_attempt.html", {"questionset": questionset, "forms": forms})
    return render(request, "courses/assessments/assessment_attempt.html", {"questionset": questionset})




