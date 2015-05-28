from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.models import Status
from courses.models import Course, Week, Lecture, News, LectureMaterials


def course_overview_view(request, course_id):
    is_enrolled = False
    # FIXME: Code smells
    if not request.user.is_anonymous() and \
            Status.objects.filter(course=course_id, user=request.user.profile, role="student"):
        is_enrolled = True
    return render(request, 'courses/preview_course.html', {"is_enrolled": is_enrolled})


def course_dashboard_view(request, course_id):
    if request.user.is_authenticated():
        return redirect("courses:news", course_id=course_id)
    else:
        return redirect("courses:course_overview", course_id=course_id)


@login_required
def news_view(request, course_id):
    feed = News.objects.filter(course=course_id).order_by("date_created")
    return render(request, 'courses/news.html', {"feed": feed})


@login_required
def lecture_view(request, course_id, week_number, lecture_number):
    course = Course.objects.get(pk=course_id)
    week = Week.objects.get(course=course, number=week_number)
    lecture = Lecture.objects.get(week=week, order_id=lecture_number)
    lecture_materials = LectureMaterials.objects.filter(lecture=lecture)

    return render(request, 'courses/lecture.html', {'lecture': lecture, "materials": lecture_materials})


@login_required
def lecture_list_view(request, course_id):
    course = Course.objects.get(pk=course_id)
    weeks = Week.objects.filter(course=course)
    # FIXME: code smells
    return render(request, 'courses/lectures.html', {'weeks': weeks})


def get_lectures(course_id):
    lectures = (Lecture.objects.filter(week=week) for week in Week.objects.filter(course=course_id))
    return lectures