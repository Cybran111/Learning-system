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
    return render(request, "courses/assessments/overview.html",
                  {"questionset": questionset, "week_id": week_id,
                   "assessment_id": assessment_id, "feedbacks": feedbacks})


@login_required
def assessment_attempt(request, course_id, week_id, assessment_id):
    questionset = QuestionSet.objects.get(course=course_id,
                                          week=Week.objects.get(course=course_id, number=week_id),
                                          number=assessment_id)

    if request.method == "GET":
        questionset = {"title": questionset.title, "description": questionset.description,
                       "questions": (QuestionForm(text=question.text, number=question.number,
                                                  answers=(answer for answer in question.possibleanswer_set.all()))
                                     for question in questionset.question_set.all())}
        return render(request, "courses/assessments/attempt.html", {"questionset": questionset})

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
                                                     mark=mark, is_finished=True,
                                                     number=StudentAnswerSet.objects.filter(
                                                         user=request.user,
                                                         questionset=questionset).count()+1
                                                     )

        for answer in request.POST.getlist("answers"):
            StudentAnswer.objects.create(answerset=answer_set,
                                         question=Question.objects.get(questionset=questionset, number=answer[0]),
                                         chosed_answer=PossibleAnswer.objects.get(question=answer[0], number=answer[2]))

        return redirect("courses:assessments:feedback", course_id=course_id, week_id=week_id,
                        assessment_id=assessment_id, feedback_id=answer_set.number)


@login_required
def assessment_feedback(request, course_id, week_id, assessment_id, feedback_id):
    questionset = QuestionSet.objects.get(course=course_id, week=week_id, number=assessment_id)
    answerset = StudentAnswerSet.objects.get(number=feedback_id, user=request.user, questionset=questionset)

    feedback = {
        "title": questionset.title,
        "description": questionset.description,
        "questions": tuple(
            ({
                "number": question.number,
                "text": question.text,
                "explanation": question.explanation,
                "answers": tuple({
                    "text": answer.text,
                    "is_correct": answer.is_correct,
                    "explanation": answer.explanation,
                    "is_chosen": bool(StudentAnswer.objects.filter(answerset=answerset,
                                                                   question=question,
                                                                   chosed_answer=answer))
                } for answer in question.possibleanswer_set.all())
            } for question in questionset.question_set.all())
        )
    }

    # for question in feedback["questions"]:
    #     for answer in question["answers"]:
    #         print answer["text"], bool(answer["is_chosen"])
    #         print answer["is_correct"]
    #         print answer["is_chosen"]

    # return render(request, "courses/assessments/feedback.html", {"feedback": answerset, "questionset": questionset})
    return render(request, "courses/assessments/feedback.html", {"feedback": feedback})