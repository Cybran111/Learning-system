__author__ = 'cybran'

from selenium import webdriver
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()
        # pass

    def test_can_sign_up(self):
        ## John wanna sign up to E-Learning System

        self.browser.get(self.live_server_url)

        # He finds the button "Sign up" and click on it
        self.browser.find_element_by_id('signup').click()

        # He writes his email..
        email_inputbox = self.browser.find_element_by_id('email')
        email_inputbox.send_keys("john@example.com")

        # and his password..
        password_inputbox = self.browser.find_element_by_id('password')
        password_inputbox.send_keys("verysecretpassword")

        # and he presses the Register button
        self.browser.find_element_by_id('register').click()

        self.fail("Finish the test")
