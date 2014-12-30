from unittest import skip
from functional_tests.base import FunctionalTest


class NewTeacherTest(FunctionalTest):

    def test_can_create_new_course(self):
        # Olga heard about a new cool course platform
        # And she decided to invest a new course for that platform

        # She goes to the site...
        self.browser.get(self.live_server_url)

        # She found a button "Create a new course" and clicks on it
        create_course = self.browser.find_element_by_id('new-course')
        create_course.click()



        # Now she is on the "Create a new course" page
        # She fills the details of her new course

        course = {'title': ("title", "My little course"),
                  'short_desc': ("short description", "Do you wanna ponies?"),
                  'full_desc': ("full description", "Friendship is Magic")
        }

        for key, value in course.iteritems():
            self.check_and_enter_to_form_element(key, *value)

        # Then she presses the "Submit" button...
        submit = self.browser.find_element_by_id('submit')
        submit.click()

        # And now she is on the page of the course and she sees all her inputs on the page
        title = self.browser.find_element_by_tag_name("h2")
        short_desc = self.browser.find_element_by_tag_name("h3")
        full_desc = self.browser.find_element_by_id("full-desc")

        elements = (title, short_desc, full_desc)

        for element, field in zip(reversed(elements), course.itervalues()):
            ## DO NOT forget that the value is in the 1st position, in the 0th position is full name of the field
            self.assertEqual(element.text, field[1])

        # And she checks that her course is available on the homepage
        self.browser.get(self.live_server_url)

        courses = self.browser.find_elements_by_class_name('list-group-item')
        self.assertIn(course['title'][1], (_course.find_element_by_tag_name('h4').text
                                           for _course in courses))
        self.assertIn(course['short_desc'][1], (_course.find_element_by_tag_name('h5').text
                                                for _course in courses))

    @skip("For removing")
    def test_can_add_new_lectures(self):
        # Olga wanna add some video lectures to her course

        # She goes to the site...
        self.browser.get(self.live_server_url)

        # She found a button "Create a new course" and clicks on it
        self.browser.find_element_by_id('new-course').click()

        # Now she is on the "Create a new course" page
        # She fills the details of her new course

        course = {'title': ("title", "My little course"),
                  'short_desc': ("short description", "Do you wanna ponies?"),
                  'full_desc': ("full description", "Friendship is Magic")
        }


        for key, value in course.iteritems():
            self.check_and_enter_to_form_element(key, *value)

        # Then she presses the "Submit" button and she is on the page of her course
        submit = self.browser.find_element_by_id('submit')
        submit.click()

        # Now she clicks on the "Add a lecture"...
        new_lecture = self.browser.find_element_by_id("manage-course")
        new_lecture.click()

        self.fail('Finish the test')

    def check_and_enter_to_form_element(self, el_name, placeholder, text):
        el = self.browser.find_element_by_css_selector('[name=%s]' % (el_name))

        self.assertEqual(
            el.get_attribute('placeholder'),
            "Enter the %s of the course" % (placeholder)
        )
        el.send_keys(text)


class NewStudentTest(FunctionalTest):
    fixtures = ["courses/fixtures/tests_data.json"]

    def test_can_go_to_course_page(self):
        ## Alice wanna to look at course

        ## She clicks on the first course
        self.browser.get(self.live_server_url)
        _list = self.browser.find_element_by_class_name('list-group')

        # getting first element in list..
        course = _list.find_element_by_class_name('list-group-item')
        course_title = course.find_element_by_tag_name("h4").text
        course_short_description = course.find_element_by_tag_name("h5").text
        course.click()

        # And she is at the course page with nice full description
        self.assertEqual(self.browser.title, course_title + " - E-Learning System")
        self.assertIn(course_title, self.browser.page_source)
        self.assertIn(course_short_description, self.browser.page_source)
        self.assertIsNotNone(self.browser.find_element_by_id("full-desc"))

    @skip("For removing")
    def test_can_browse_lectures_by_the_week(self):
        # Alice wanna see the course topics and lectures

        # She goes to the site...
        self.browser.get(self.live_server_url)

        _list = self.browser.find_element_by_class_name('list-group')

        # ...she goes to the first course and click on it...
        _list.find_element_by_class_name("list-group-item").click()

        # ...she finds the element that redirects her to the course lecture list...
        self.browser.find_element_by_id('lecture-page').click()


        # She sees that page has a week list with  lecture lists on every week
        weeks = self.browser.find_elements_by_class_name("panel")





