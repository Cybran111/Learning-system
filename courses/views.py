from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from courses.forms import NewCourseForm, NewLectureForm
from courses.models import Course, Week, Lecture, News, LectureMaterials


def course_overview_view(request, course_id):
    return render(request, 'courses/preview_course.html')


def course_dashboard_view(request, course_id):
    if request.user.is_authenticated():
        return redirect("courses:news", course_id=course_id)
    else:
        return redirect("courses:course_overview", course_id=course_id)


@login_required
def news_view(request, course_id):
    # News.objects.create(title=course_id,
    #                     text="some text",
    #                     course=Course.objects.get(pk=course_id)
    #                     )
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


def manage_course_view(request, course_id):
    return render(request, 'courses/manage.html', {'lectures_by_week': get_lectures(course_id)})


def create_course_view(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            new_course = Course()
            new_course.title = request.POST['title']
            new_course.short_description = request.POST['short_desc']
            new_course.full_description = request.POST['full_desc']
            new_course.save()
            return redirect(reverse('courses:course_overview', args=(new_course.id,)))
    else:
        form = NewCourseForm()
        return render(request, 'courses/new_course.html', {"new_course_form": form})


@require_POST
def manage_week_view(request, course_id):
    course = Course.objects.get(pk=course_id)
    week_count = Week.objects.filter(course=course).count()
    Week.objects.create(course=course, number=week_count + 1)

    return redirect("courses:manage", course_id=course.id)


def manage_lecture_view(request, course_id, week_number):
    if request.method == 'POST':  # If the form has been submitted...

        form = NewLectureForm(request.POST)

        if form.is_valid():  # All validation rules pass
            # NOTE: Monkeycode?
            course = Course.objects.get(pk=course_id)
            week = Week.objects.get(course=course, number=week_number)

            new_lecture = form.save(commit=False)

            new_lecture.week = week
            new_lecture.order_id = Lecture.objects.filter(week=week).count() + 1
            new_lecture.embed_video_url = "https://www.youtube.com/embed/" + new_lecture.video_url[-11:]

            new_lecture.save()
            return redirect("courses:manage", course_id=course.id)

    else:
        form = NewLectureForm()  # An unbound form

    return render(request, 'courses/new_lecture.html', {'form': form, })


def get_lectures(course_id):
    lectures = (Lecture.objects.filter(week=week) for week in Week.objects.filter(course=course_id))
    return lectures