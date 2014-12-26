from course.models import Course

__author__ = 'cybran'

from selenium import webdriver
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):

        course_data = (
            {"title": "Introduction to Python", "description": "Lets learn Python!"},
            {"title": "Introduction to TDD", "description": "New methodology. New problem"},
        )

        for course in course_data:
            Course.objects.create(title=course["title"], description=course["description"])



        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_can_look_at_course_list(self):
        # Alice has heard about a cool new course platform.
        # She goes to check out its homepage

        self.browser.get(self.live_server_url)

        # She notices the course list with title and description of every course
        _list = self.browser.find_element_by_class_name('list-group')
        courses = _list.find_elements_by_class_name("list-group-item")
        self.assertIn("Introduction to Python", courses[0].find_element_by_tag_name("h4").text)
        self.assertIn("Lets learn Python!", courses[0].find_element_by_tag_name("h5").text)

        self.assertIn("Introduction to TDD", courses[1].find_element_by_tag_name("h4").text)
        self.assertIn("New methodology. New problem", courses[1].find_element_by_tag_name("h5").text)

    def test_can_go_to_course_page(self):

        self.browser.get(self.live_server_url)
        _list = self.browser.find_element_by_class_name('list-group')
        first_course = _list.find_element_by_class_name('list-group-item')
        first_course.click()
