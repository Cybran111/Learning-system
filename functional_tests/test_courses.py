from courses.models import Course
from functional_tests.base import FunctionalTest


class NewTeacherTest(FunctionalTest):
    def setUp(self):

        self.course = {'title': ("title", "My little course"),
                       'short_desc': ("short description", "Do you wanna ponies?"),
                       'full_desc': ("full description", "Friendship is Magic")
        }

        super(NewTeacherTest, self).setUp()

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

        for key, value in self.course.iteritems():
            self.check_and_enter_to_form_element(key, *value)

        # Then she presses the "Submit" button...
        submit = self.browser.find_element_by_id('submit')
        submit.click()

        # And now she is on the page of the course and she sees all her inputs on the page
        title = self.browser.find_element_by_tag_name("h2")
        short_desc = self.browser.find_element_by_tag_name("h3")
        full_desc = self.browser.find_element_by_id("full-desc")

        elements = (title, short_desc, full_desc)

        for element, field in zip(reversed(elements), self.course.itervalues()):
            ## DO NOT forget that the value is in the 1st position, in the 0th position is full name of the field
            self.assertEqual(element.text, field[1])

        # And she checks that her course is available on the homepage
        self.browser.get(self.live_server_url)

        courses = self.browser.find_elements_by_class_name('list-group-item')
        self.assertIn(self.course['title'][1], (_course.find_element_by_tag_name('h4').text
                                                for _course in courses))
        self.assertIn(self.course['short_desc'][1], (_course.find_element_by_tag_name('h5').text
                                                     for _course in courses))

    def test_can_add_new_lectures(self):
        # Olga wanna add some video lectures to her course

        # She goes to the site...
        self.browser.get(self.live_server_url)

        # She found a button "Create a new course" and clicks on it
        self.browser.find_element_by_id('new-course').click()

        # Now she is on the "Create a new course" page
        # She fills the details of her new course

        for key, value in self.course.iteritems():
            self.check_and_enter_to_form_element(key, *value)

        # Then she presses the "Submit" button and she is on the page of her course
        submit = self.browser.find_element_by_id('submit')
        submit.click()

        # Now she clicks on the "Add a lecture"...
        new_lecture = self.browser.find_element_by_id("new-lecture")
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
    def setUp(self):
        self.course_data = (
            {"title": "Introduction to Python",
             "short_description": "Lets learn Python!",
             'full_description': "Some expanded description",
             "weeks": (
                 (('Introduction to the Course'), ("Object-oriented programming. part 1")),
                 (('Object-oriented programming. part 2'),),
             )
            },
            {"title": "Introduction to TDD",
             "short_description": "New methodology. New problem",
             "full_description": "Yet another full description",
             "weeks": (
                 (('Introduction to the Course'), ("Red-green-refactor")),
                 (('No code without a test'), ('Slow developing process, but effective in long range')),
             )
            },
        )

        for course in self.course_data:
            Course.objects.create(title=course["title"],
                                  short_description=course["short_description"],
                                  full_description=course['full_description'])

        super(NewStudentTest, self).setUp()

    def test_can_look_at_course_list(self):
        # Alice has heard about a new cool course platform.
        # She goes to check out its homepage

        self.browser.get(self.live_server_url)

        # She notices the course list with title and short description of every course
        _list = self.browser.find_element_by_class_name('list-group')
        courses = _list.find_elements_by_class_name("list-group-item")

        # time.sleep(60)
        for data, course in zip(self.course_data, courses):
            self.assertIn(data["title"], course.find_element_by_tag_name("h4").text)
            self.assertIn(data["short_description"], course.find_element_by_tag_name("h5").text)

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

        # Find the correct full desc of the course
        course_full_description = tuple(course for course in self.course_data if course['title'] == course_title)[0][
            'full_description']

        ## And she is at the course page
        self.assertEqual(self.browser.title, course_title + " - E-Learning System")
        self.assertIn(course_title, self.browser.page_source)
        self.assertIn(course_short_description, self.browser.page_source)
        self.assertIn(course_full_description, self.browser.page_source)


    def test_can_browse_lectures_by_the_week(self):
        # Alice wanna see the course topics and lectures

        # She goes to the site...
        self.browser.get(self.live_server_url)

        _list = self.browser.find_element_by_class_name('list-group')

        # ...she goes to the first course and click on it...
        _list.find_element_by_class_name("list-group-item").click()

        # ...she finds the element that redirects her to the course lecture list...
        self.browser.find_element_by_id('lecture_page').click()


        # She sees that page has a week list with nested lecture lists on every week
        week_list = self.browser.find_element_by_id("weeks-list")
        weeks = week_list.find_elements_by_class_name("list-group-item")
        for week_number, week in enumerate(weeks):
            self.assertEqual("Week %d" % (week_number), week.text)

            lecture_list = week.find_element_by_class_name("lecture-list")
            lectures = lecture_list.find_elements_by_class_name('list-group-item')

            for lecture_number, lecture in enumerate(lectures):
                self.assertEqual("%d: %s" % (lecture_number, self.course_data['weeks'][week_number][lecture_number]),
                                 lecture.text)



