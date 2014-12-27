from courses.models import Course
from functional_tests.base import FunctionalTest


class NewTeacherTest(FunctionalTest):
    def test_can_create_new_course(self):
        # Olga heard about a new cool course platform
        # And she decided to invest a new course for that platform

        # She goes to the site...
        self.browser.get(self.live_server_url)

        # She found a button "Create a new course" and clicks to it
        create_course = self.browser.find_element_by_id('new-course')
        create_course.click()

        # Now she is on the "Create a new course"
        # She fills the details of her new course
        self.check_and_enter_to_form_element('title', 'title', 'My little course')
        self.check_and_enter_to_form_element('short_desc',
                                             'short description',
                                             'Do you wanna ponies?')
        self.check_and_enter_to_form_element('full_desc',
                                             'full description',
                                             "Friendship is Magic", el_view='textarea')

        # Then she presses the "Submit" button...
        submit = self.browser.find_element_by_id('submit')
        submit.click()

        # And now she is on the page of the course and she sees all her inputs on the page


        # And she checks that her course is available on the homepage
        self.browser.get(self.live_server_url)

        courses = self.browser.find_elements_by_class_name('list-group-item')
        self.assertIn("My little course", (course.find_element_by_tag_name('h4').text for course in courses))
        self.assertIn("Do you wanna ponies?", (course.find_element_by_tag_name('h5').text for course in courses))

    def check_and_enter_to_form_element(self, el_name, placeholder, text, el_view='input'):
        el = self.browser.find_element_by_css_selector('%s[name=%s]' % (el_view, el_name))

        self.assertEqual(
            el.get_attribute('placeholder'),
            "Enter the %s of the course" % (placeholder)
        )
        el.send_keys(text)


class NewStudentTest(FunctionalTest):
    def setUp(self):
        course_data = (
            {"title": "Introduction to Python", "short_description": "Lets learn Python!"},
            {"title": "Introduction to TDD", "short_description": "New methodology. New problem"},
        )

        for course in course_data:
            Course.objects.create(title=course["title"], short_description=course["short_description"])

        super(NewStudentTest, self).setUp()

    def test_can_look_at_course_list(self):
        # Alice has heard about a new cool course platform.
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


