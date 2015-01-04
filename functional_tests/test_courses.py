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





