from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.test import TestCase
from django.utils.html import escape

from courses.forms import NewLectureForm
from courses.models import Course, Week, Lecture


PK = 1


class CourseTest(TestCase):
    fixtures = ['tests_data.json']


class CRUDTest(CourseTest):
    # TODO: Need to rewrite accordingly to authenticated user
    # def test_can_get_lecture(self):
    #     course = Course.objects.get(pk=PK)
    #     week = Week.objects.get(course=course, number=PK)
    #     lecture = Lecture.objects.get(week=week, order_id=PK)
    #
    #     response = self.client.get('/courses/%s/week/%s/lecture/%s/' % (PK, PK, PK))
    #     self.assertContains(response, lecture.embed_video_url)

    # TODO: Need to rewrite accordingly to authenticated user
    # def test_can_get_course_lectures_page(self):
    #     response = self.client.get('/courses/%s/lectures/' % PK)
    #     course = Course.objects.get(pk=PK)
    #
    #     lectures = (reverse("courses:lecture", args=(course.id, week.number, lecture.order_id)) for week in
    #                 course.week_set.all() for lecture in week.lecture_set.all())
    #
    #     for lecture in lectures:
    #         self.assertContains(response, lecture)

    def test_can_get_manage_page(self):
        course = Course.objects.get(pk=PK)
        response = self.client.get('/courses/%s/manage/' % (course.id))

        for lecture in self.get_lectures(course):
            self.assertContains(response, escape(lecture.title))

    def test_can_add_week(self):
        course = Course.objects.get(pk=PK)
        weeks_count = self.get_weeks_count(course)
        response = self.client.post('/courses/%s/manage/week/' % (course.id))

        self.assertRedirects(response, "/courses/%s/manage/" % (course.id))
        self.assertNotEqual(weeks_count, self.get_weeks_count(course))

    def test_can_add_lecture(self):
        course = Course.objects.get(pk=PK)
        week = Week.objects.filter(course=course)[0]
        lectures_count = self.get_lectures_count(week)
        response = self.client.post('/courses/%s/manage/week/%s/' % (course.id, week.number),
                                    {"title": "My little lecture",
                                     "video_url": "https://www.youtube.com/watch?v=sm0QQO-WZlM", })
        self.assertRedirects(response, "/courses/%s/manage/" % (course.id))
        self.assertNotEqual(lectures_count, self.get_lectures_count(week))

    def test_can_get_course_overview_page(self):
        course = Course.objects.get(pk=PK)
        response = self.client.get('/courses/%s/overview/' % (course.id))

        self.assertContains(response, escape(course.title))
        self.assertContains(response, escape(course.short_description))
        self.assertContains(response, escape(course.full_description))

    def get_weeks_count(self, course):
        return Week.objects.filter(course=course).count()

    def get_lectures_count(self, week):
        return Lecture.objects.filter(week=week).count()

    def get_lectures(self, course):
        lectures = (lecture for week in Week.objects.filter(course=course) for lecture in
                    Lecture.objects.filter(week=week))
        return lectures


class ListTest(CourseTest):
    def test_homepage_returns_correct_page_with_list(self):
        response = self.client.get('/')
        courses = Course.objects.all()
        expected_html = render_to_string('dashboard/homepage.html', {"courses": courses})
        self.assertEqual(response.content.decode(), expected_html)


class SaveCourseTest(TestCase):
    def setUp(self):
        self.course_data = {'title': 'My course', 'short_desc': 'A tiny course', 'full_desc': "A REALLY tiny course"}

    def test_redirect_to_coursepage_when_created(self):
        response = self.client.post('/courses/new', data=self.course_data)
        self.assertRedirects(response, 'courses/1/overview/')

    def test_can_save_new_course(self):
        self.client.post('/courses/new', data=self.course_data, )
        self.assertEqual(Course.objects.count(), 1)
        new_course = Course.objects.first()
        self.assertEqual(new_course.title, 'My course')
        self.assertEqual(new_course.short_description, 'A tiny course')
        self.assertEqual(new_course.full_description, 'A REALLY tiny course')


class ModelsTest(TestCase):
    def test_course_can_holds_weeks_and_lectures(self):
        course = Course()
        course.title = "A little title"
        course.save()

        week = Week()
        week.course = course
        week.number = 1
        week.save()

        lecture = Lecture()
        lecture.title = "My lecture"
        lecture.video_url = "https://www.youtube.com/watch?v=lXn7XKLA6Vg"
        lecture.week = week
        lecture.order_id = 1
        lecture.save()

        self.assertEqual(week, Week.objects.get(course=course))
        self.assertEqual(lecture, Lecture.objects.get(week=week))

    def test_lecture_cant_have_not_youtube_url(self):
        course = Course()
        course.title = "Yet another title"
        course.save()

        week = Week()
        week.number = 1
        week.course = course
        week.save()

        data = {"title": "My lecture", "week": week, "order_id": 1,
                "embed_video_url": "https://www.youtube.com/embed/lXn7XKLA6Vg", }

        # For easy use
        _assert_true = self.assertTrue
        _assert_false = self.assertFalse
        urls = (
            ("http://habrahabr.ru", _assert_false), ("https://www.google.com.ua/", _assert_false),
            ("https://www.youtube.com/watch?v=lXn7XKLA6Vg", _assert_true)
        )

        for url, suggested_func in urls:
            data["video_url"] = url
            lecture = NewLectureForm(data=data)
            suggested_func(lecture.is_valid())