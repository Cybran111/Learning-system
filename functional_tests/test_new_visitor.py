from course.models import Course
from functional_tests.base import FunctionalTest


class NewVisitorTest(FunctionalTest):


    def setUp(self):
        course_data = (
            {"title": "Introduction to Python", "short_description": "Lets learn Python!"},
            {"title": "Introduction to TDD", "short_description": "New methodology. New problem"},
        )

        for course in course_data:
            Course.objects.create(title=course["title"], short_description=course["short_description"])

        super(NewVisitorTest, self).setUp()

    def test_can_look_at_course_list(self):
        # Alice has heard about a cool new course platform.
        # She goes to check out its homepage

        self.browser.get(self.live_server_url)

        # She notices the course list with title and short description of every course
        _list = self.browser.find_element_by_class_name('list-group')
        courses = _list.find_elements_by_class_name("list-group-item")

        self.assertIn("Introduction to Python", courses[0].find_element_by_tag_name("h4").text)
        self.assertIn("Lets learn Python!", courses[0].find_element_by_tag_name("h5").text)

        self.assertIn("Introduction to TDD", courses[1].find_element_by_tag_name("h4").text)
        self.assertIn("New methodology. New problem", courses[1].find_element_by_tag_name("h5").text)

    def test_can_go_to_course_page(self):

        ## Alice wanna to look at course and enroll to it

        ## She clicks on the first course
        self.browser.get(self.live_server_url)
        _list = self.browser.find_element_by_class_name('list-group')

        # getting first element
        course = _list.find_element_by_class_name('list-group-item')
        course_title = course.find_element_by_tag_name("h4").text
        course_short_description = course.find_element_by_tag_name("h5").text

        course.click()

        ## And she is at the course page
        self.assertEqual(self.browser.title, "Introduction to Python - E-Learning System")
        self.assertIn(course_title, self.browser.page_source)
        self.assertIn(course_short_description, self.browser.page_source)


