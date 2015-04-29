from functional_tests.base import FunctionalTest


class NewStudentTest(FunctionalTest):
    fixtures = ["courses/fixtures/tests_data.json"]

    # # FIXME: separate to several tests
    # def test_can_watch_lecture_of_course(self):
    #     ## Alice wanna to look at course
    #
    #     # She registering...
    #     self.browser.get(self.live_server_url)
    #     self.browser.find_element_by_id("register").click()
    #
    #     username = self.browser.find_element_by_id("id_username")
    #     username.send_keys("Alice")
    #
    #     email = self.browser.find_element_by_id("id_email")
    #     email.send_keys("alice@example.com")
    #
    #     password = self.browser.find_element_by_id("id_password")
    #     password.send_keys("asecretpassword")
    #
    #     self.browser.find_element_by_id("submit").click()
    #
    #     ## She clicks on the first course
    #     _list = self.browser.find_element_by_class_name('list-group')
    #
    #     # getting first element in list..
    #     course = _list.find_element_by_class_name('list-group-item')
    #     course_title = course.find_element_by_tag_name("h4").text
    #     course_short_description = course.find_element_by_tag_name("h5").text
    #     course.click()
    #
    #     # And she at the course page with nice full description
    #     self.assertEqual(self.browser.title, course_title + " - E-Learning System")
    #     self.assertIn(course_title, self.browser.page_source)
    #     self.assertIn(course_short_description, self.browser.page_source)
    #     self.assertIsNotNone(self.browser.find_element_by_id("full-desc"))
    #
    #     # Now she clicks on the "Enroll" button
    #     self.browser.find_element_by_id("enroll").click()
    #
    #     # And she is on the lecture list page
    #     self.assertIsNotNone(self.browser.find_element_by_id("weeks-list"))
    #
    #     # She decided to go to the lecture
    #     week = self.browser.find_element_by_class_name("week")
    #     week.find_element_by_class_name("title").click()
    #     week.find_element_by_class_name("list-group-item").click()
    #
    #     # She watching the video lecture with pleasure
    #     self.browser.find_element_by_id("video")
    #
    #     # When she finished watching, she goes to her accounts to see that she enrolled to this course
    #     self.browser.find_element_by_id("user-accounts").click()
    #
    #     enrolled_list = self.browser.find_element_by_id("enrolled-courses")
    #     enrolled_course = enrolled_list.find_element_by_class_name("course-item")
    #     self.assertEqual("Nulla mollis neque eget lorem", enrolled_course.find_element_by_tag_name("h4").text)