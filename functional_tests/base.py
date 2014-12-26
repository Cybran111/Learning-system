from course.models import Course

__author__ = 'cybran'

from selenium import webdriver
from django.test import LiveServerTestCase

class FunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

