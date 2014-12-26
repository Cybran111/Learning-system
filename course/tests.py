from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.core.urlresolvers import resolve
from course.views import home_page
from course.models import Course

# Create your tests here.
class HomePageTest(TestCase):

    def test_homepage_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homepage_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        courses = Course.objects.all()
        expected_html = render_to_string('homepage.html', {"courses": courses})
        self.assertEqual(response.content.decode(), expected_html)