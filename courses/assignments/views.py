from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.core.signing import SignatureExpired, loads, dumps
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_POST
from courses.assignments.models import Feedback, Assignment
from courses.models import Week, Course


@login_required
def assignments_view(request, course_id):

    weeks = Week.objects.filter(course=course_id)
    return render(request, "courses/assignments/assignments.html", {'weeks': weeks})


@login_required
def assignment_view(request, course_id, week_id, assignment_id):

    # assignment = models.ForeignKey(Assignment)
    # student = models.ForeignKey(User)
    # attempt = models.PositiveIntegerField()
    # mark = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    if request.method == 'GET':
        assignment = Assignment.objects.get(course=course_id, week=week_id, number=assignment_id)
        feedbacks = Feedback.objects.filter(student=request.user, assignment=assignment)
        return render(request, "courses/assignments/assignment.html", {"assignment": assignment,
                                                                       "feedbacks": feedbacks})

    elif request.method == 'POST':
        pass


@require_POST
def feedback_view(request, feedback_route):

    try:
        feedback = loads(feedback_route, max_age=timedelta(minutes=2))
    except SignatureExpired:
        return HttpResponseBadRequest()

    feedback_object = Feedback(assignment=feedback["assignment"],
                            student=feedback["student"],
                            attempt=feedback["attempt"],
                            mark=request.POST["mark"])
    if feedback_object.full_clean():
        feedback_object.save()
        return HttpResponse()

    return HttpResponseBadRequest()