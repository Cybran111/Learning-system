from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.test import TestCase
from django.core.urlresolvers import resolve

from courses.views import home_page
from courses.models import Course, Week, Lecture




# Create your tests here.
class CourseListTest(TestCase):
    def setUp(self):
        course_data = (
            {
                "title": "Introduction to Python",
                "short_description": "Lets learn Python!",
                "full_description": "Some description",
                # lectures by week
                'lectures': (
                    (
                        "https://www.youtube.com/watch?v=T3l0Co9bHJg",
                        "https://www.youtube.com/watch?v=vYP4KqpsvFs"
                    ),
                    (
                        "https://www.youtube.com/watch?v=sm0QQO-WZlM",
                        "https://www.youtube.com/watch?v=2lWYkj_EQw0"
                    )
                ),
            },
            {
                "title": "Introduction to TDD",
                "short_description": "New methodology. New problem",
                "full_description": "Yet another full description",
                'lectures': (

                    (
                        "https://www.youtube.com/watch?v=sm0QQO-WZlM",
                        "https://www.youtube.com/watch?v=2lWYkj_EQw0"
                    ),
                    (
                        "https://www.youtube.com/watch?v=T3l0Co9bHJg",
                        "https://www.youtube.com/watch?v=vYP4KqpsvFs"
                    )
                ),
            },
        )

        for course in course_data:
            current_course = Course.objects.create(title=course["title"],
                                                   short_description=course["short_description"],
                                                   full_description=course["full_description"])

            for number, week in enumerate(course["lectures"]):
                current_week = Week.objects.create(number=number, course=current_course)

                for lecture_url in week:
                    Lecture.objects.create(video_url=lecture_url, week=current_week)

    def test_homepage_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homepage_returns_correct_page_with_list(self):
        response = self.client.get('/')
        courses = Course.objects.all()
        expected_html = render_to_string('homepage.html', {"courses": courses})
        self.assertEqual(response.content.decode(), expected_html)

    def test_can_get_course_lectures_page(self):
        response = self.client.get('/courses/1/lectures/')
        course = Course.objects.get(pk=1)

        lectures = (lecture for week in Week.objects.filter(course=course)
                    for lecture in Lecture.objects.filter(week=week))

        for lecture in lectures:
            self.assertContains(response, lecture.video_url)


    def test_can_get_course_page(self):
        course = Course.objects.get(pk=1)
        response = self.client.get('/courses/%s/' % (course.id))
        self.assertContains(response, course.title)
        self.assertContains(response, course.short_description)
        self.assertContains(response, course.full_description)


class SaveCourseTest(TestCase):
    def setUp(self):
        self.course_data = {'title': 'My course', 'short_desc': 'A tiny course', 'full_desc': "A REALLY tiny course"}

    def test_redirect_to_coursepage_when_created(self):
        response = self.client.post(
            '/courses/new',
            data=self.course_data
        )
        self.assertRedirects(response, 'courses/1/')


    def test_can_save_new_course(self):
        self.client.post(
            '/courses/new',
            data=self.course_data,
        )
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
        lecture.video_url = "https://www.youtube.com/watch?v=lXn7XKLA6Vg"
        lecture.week = week
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

        lecture = Lecture()
        lecture.week = week

        lecture.video_url = "http://habrahabr.ru"
        self.assertRaises(ValidationError, lecture.full_clean)

        lecture.video_url = "https://www.google.com.ua/"
        self.assertRaises(ValidationError, lecture.full_clean)

        lecture.video_url = "https://www.youtube.com/watch?v=lXn7XKLA6Vg"
        lecture.full_clean()