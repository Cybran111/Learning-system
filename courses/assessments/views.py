from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from courses.assessments.forms import QuestionForm
from courses.assessments.models import QuestionSet, StudentAnswerSet, StudentAnswer, Question, PossibleAnswer
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

    if request.method == "GET":
        questionset = {"title": questionset.title, "description": questionset.description,
                       "questions": (QuestionForm(text=question.text, number=question.number, answers=(answer for answer in question.possibleanswer_set.all()))
                                     for question in questionset.question_set.all())}
        return render(request, "courses/assessments/assessment_attempt.html", {"questionset": questionset})

    if request.method == "POST":

        mark = 0
        # FIXME: Monkey code!
        for question in questionset.question_set.all():
            for possible_answer in question.possibleanswer_set.all():
                question_answer_id = "%d-%d" % (question.number, possible_answer.number)

                if (possible_answer.is_correct and question_answer_id in request.POST.getlist("answers")) or \
                        (not possible_answer.is_correct and question_answer_id not in request.POST.getlist("answers")):
                    mark += question.value / question.possibleanswer_set.all().count()

        answer_set = StudentAnswerSet.objects.create(user=request.user, questionset=questionset,
                                                     mark=mark, is_finished=True)

        for answer in request.POST.getlist("answers"):
            StudentAnswer.objects.create(answerset=answer_set,
                                         question=Question.objects.get(questionset=questionset, number=answer[0]),
                                         chosed_answer=PossibleAnswer.objects.get(question=answer[0], number=answer[2]))

        return redirect("courses:news", course_id=course_id)



