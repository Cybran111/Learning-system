# Create your tests here.
from django.contrib.auth import SESSION_KEY
from django.test import TestCase
from django.contrib.auth.models import User

from courses.models import Course
from dashboard.models import Profile


PK = 1


class UserInteractionTest(TestCase):
    fixtures = ["tests_data.json"]

    def test_can_enroll(self):
        self.client.post('/dashboard/register/',
                         {
                             'username': 'john',
                             'email': 'john@lennon.com',
                             "password": "johnpassword"
                         })
        user = User.objects.get(username="john")

        course = Course.objects.get(pk=PK)

        self.client.post('/dashboard/enroll/', {"course": course.id})
        profile = Profile.objects.get(user=user)

        self.assertIn(course, profile.courses.all())

    def test_can_register(self):
        self.client.post('/dashboard/register/',
                         {
                             'username': 'john',
                             'email': 'john@lennon.com',
                             "password": "johnpassword"
                         })
        user = User.objects.get(username="john")
        self.assertEqual(self.client.session[SESSION_KEY], user.pk)

    def test_login_allow_with_good_cred(self):
        user = User.objects.create_user('john', 'john@lennon.com', 'johnpassword')
        self.client.post('/dashboard/login/', {'username': 'john', "password": "johnpassword"})
        self.assertEqual(self.client.session[SESSION_KEY], user.pk)


def test_login_deny_with_bad_cred(self):
    self.client.post('/dashboard/login/', {'username': 'john', "password": "johnpassword"})
    self.assertNotIn(SESSION_KEY, self.client.session)