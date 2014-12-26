from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.core.urlresolvers import resolve
from course.views import home_page, course_view
from course.models import Course

# Create your tests here.
class HomePageTest(TestCase):

    def setUp(self):
        course_data = (
            {"title": "Introduction to Python", "short_description": "Lets learn Python!"},
            {"title": "Introduction to TDD", "short_description": "New methodology. New problem"},
        )

        for course in course_data:
            Course.objects.create(title=course["title"], short_description=course["short_description"])

    def test_homepage_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homepage_returns_correct_page_with_list(self):
        request = HttpRequest()
        response = home_page(request)
        courses = Course.objects.all()
        expected_html = render_to_string('homepage.html', {"courses": courses})
        self.assertEqual(response.content.decode(), expected_html)

    def test_can_get_course_page(self):
        course_id = 1
        response = self.client.get('/courses/%s/' % (course_id))
        course = Course.objects.get(pk=course_id)
        self.assertContains(response, course.title)
        self.assertContains(response, course.short_description)
        self.assertContains(response, course.full_description)
