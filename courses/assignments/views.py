from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.signing import SignatureExpired, loads, dumps
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import requests
from Learning_system.settings import ASSIGNMENT_FEEDBACK_TIMEOUT
from courses.assignments.forms import NewSolutionForm
from courses.assignments.models import Feedback, Assignment
from courses.models import Week


@login_required
def assignments_view(request, course_id):
    weeks = Week.objects.filter(course=course_id)
    return render(request, "courses/assignments/assignments.html", {'weeks': weeks})


@login_required
def assignment_view(request, course_id, week_id, assignment_id):
    assignment = Assignment.objects.get(course=course_id, week=Week.objects.get(course=course_id, number=week_id),
                                        number=assignment_id)
    feedbacks = Feedback.objects.filter(student=request.user, assignment=assignment)

    if request.method == 'GET':
        form = NewSolutionForm()

    elif request.method == 'POST':
        form = NewSolutionForm(request.POST, request.FILES)
        if form.is_valid():
            feedback = Feedback.objects.create(assignment=assignment, student=request.user,
                                               attempt=feedbacks.count()+1)
            # TODO: Should use Celery for this task
            url = request.build_absolute_uri(reverse('courses:assignments:feedback', args=(
                course_id, dumps(
                    {
                        "assignment": feedback.assignment.id,
                        "student": feedback.student.id,
                        "attempt": feedback.attempt
                    })
            )))

            requests.post(assignment.checker_url, data={"url": url, "timeout": ASSIGNMENT_FEEDBACK_TIMEOUT},
                          files=request.FILES)

    return render(request, "courses/assignments/assignment.html",
                  {"assignment": assignment, "feedbacks": feedbacks, "solution": form})


@require_POST
@csrf_exempt
def feedback_view(request, course_id, feedback_route):
    try:
        feedback = loads(feedback_route, max_age=ASSIGNMENT_FEEDBACK_TIMEOUT)
    except SignatureExpired:
        return HttpResponseBadRequest()

    feedback_object = Feedback.objects.get(assignment=feedback["assignment"],
                                           student=feedback["student"],
                                           attempt=feedback["attempt"],)
    feedback_object.mark = request.POST["mark"]
    try:
        feedback_object.full_clean()
    except ValidationError:
        return HttpResponseBadRequest()

    feedback_object.save()
    return HttpResponse()