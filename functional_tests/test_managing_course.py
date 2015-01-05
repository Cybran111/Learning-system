from unittest import skip

from functional_tests.base import FunctionalTest


__author__ = 'cybran'


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

        course = {
            'title': "My little course",
            'short_desc': "Do you wanna ponies?",
            'full_desc': "Friendship is Magic"
        }

        for key, value in course.iteritems():
            self.enter_to_form_element(key, value)

        # Then she presses the "Submit" button...
        submit = self.browser.find_element_by_id('submit')
        submit.click()

        # And now she is on the page of the course and she sees all her inputs on the page
        title = self.browser.find_element_by_tag_name("h2")
        short_desc = self.browser.find_element_by_tag_name("h3")
        full_desc = self.browser.find_element_by_id("full-desc")

        elements = (title, short_desc, full_desc)

        for element, course_text in zip(reversed(elements), course.itervalues()):
            ## DO NOT forget that the value is in the 1st position, in the 0th position is full name of the field
            self.assertEqual(element.text, course_text)

        # And she checks that her course is available on the homepage
        self.browser.get(self.live_server_url)

        new_course = self.browser.find_element_by_class_name('list-group-item')
        self.assertIn(course['title'], new_course.find_element_by_tag_name('h4').text)
        self.assertIn(course['short_desc'], new_course.find_element_by_tag_name('h5').text)

    def test_can_add_new_week_and_lecture(self):
        # Olga wanna add some video lectures to her course

        # She goes to the site...
        self.browser.get(self.live_server_url)

        # She found a button "Create a new course" and clicks on it
        self.browser.find_element_by_id('new-course').click()

        # Now she is on the "Create a new course" page
        # She fills the details of her new course

        course = {
            'title': "My little course",
            'short_desc': "Do you wanna ponies?",
            'full_desc': "Friendship is Magic"
        }

        for key, value in course.iteritems():
            self.enter_to_form_element(key, value)

        # Then she presses the "Submit" button
        submit = self.browser.find_element_by_id('submit')
        submit.click()

        # She is on the Course page
        # Now she clicks on the "Manage course"...
        self.browser.find_element_by_id("manage-course").click()


        # She sees that there are no course weeks right now...
        self.assertFalse(self.browser.find_elements_by_class_name("week"))

        # ..so let's add a new one!
        self.browser.find_element_by_id("add-week").click()

        # And new week was added
        new_week = self.browser.find_element_by_class_name("week")
        self.assertEqual(new_week.text, "Week 1")

        # She decided to add a new lecture to that week
        new_week.find_element_by_class_name("add-lecture").click()

        # She is on the New Lecture form
        # She puts a lecture title..
        title_input = self.browser.find_element_by_id("course-title")
        title_input.send_keys("An introduction to the course")

        # ..then she puts URL of the lecture..
        url_input = self.browser.find_element_by_id("course-video")
        url_input.send_keys("http://vimeo.com/14612897")

        # After that, she clicks on Submit..
        submit = self.browser.find_element_by_id("submit")
        submit.click()

        # Woops! Only Youtube video allowed :(
        # Olga received a validation error
        error = self.get_error_element()
        self.assertEqual(error.text, "Only videos from YouTube are allowed")

        # "OK!" - Olga thought and puts a new URL to that field
        url_input.send_keys("https://www.youtube.com/watch?v=E5rFiDmSPbY")
        submit.click()

        # Done! Now Olga is on the Manage Lecture page
        # And she sees that the new lecture is on the page
        self.assertInHTML("An introduction to the course", self.browser.page_source)

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def enter_to_form_element(self, el_name, text):
        el = self.browser.find_element_by_css_selector('[name=%s]' % (el_name))
        el.send_keys(text)