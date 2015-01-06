from unittest import skip
from functional_tests.base import FunctionalTest



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

        # Now she clicks on the "Enroll" button
        self.browser.find_element_by_id("enroll").click()


        # And she is on the lecture list page
        self.assertIsNotNone(self.browser.find_element_by_id("weeks-list"))

        # She decided to go to the lecture
        week = self.browser.find_element_by_class_name("week")
        week.find_element_by_class_name("title").click()
        week.find_element_by_class_name("list-group-item").click()

        # She watching the video lecture with pleasure
        self.browser.find_element_by_id("video")

        # When she finished watching, she goes to her dashboard to see that this course
        self.fail("Finish the test")

