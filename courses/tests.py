from django.test import TestCase
from django.utils.html import escape

from courses.models import Course, Week, Lecture


PK = 1


class CourseTest(TestCase):
    fixtures = ['tests_data.json']


# class CRUDTest(CourseTest):
#     def test_can_get_course_overview_page(self):
#         course = Course.objects.get(pk=PK)
#         response = self.client.get('/courses/%s/overview/' % (course.id))
#
#         self.assertContains(response, escape(course.title))
#         self.assertContains(response, escape(course.short_description))
#         self.assertContains(response, escape(course.full_description))
#
#     def get_weeks_count(self, course):
#         return Week.objects.filter(course=course).count()
#
#     def get_lectures_count(self, week):
#         return Lecture.objects.filter(week=week).count()
#
#     def get_lectures(self, course):
#         lectures = (lecture for week in Week.objects.filter(course=course) for lecture in
#                     Lecture.objects.filter(week=week))
#         return lectures


class SaveCourseTest(TestCase):
    def setUp(self):
        self.course_data = {'title': 'My course', 'short_desc': 'A tiny course', 'full_desc': "A REALLY tiny course"}


# class ModelsTest(TestCase):
#     def test_course_can_holds_weeks_and_lectures(self):
#         course = Course()
#         course.title = "A little title"
#         course.save()
#
#         week = Week()
#         week.course = course
#         week.number = 1
#         week.save()
#
#         lecture = Lecture()
#         lecture.title = "My lecture"
#         lecture.video_url = "https://www.youtube.com/watch?v=lXn7XKLA6Vg"
#         lecture.week = week
#         lecture.order_id = 1
#         lecture.save()
#
#         self.assertEqual(week, Week.objects.get(course=course))
#         self.assertEqual(lecture, Lecture.objects.get(week=week))