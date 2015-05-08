# Create your tests here.
from django.contrib.auth import SESSION_KEY
from django.test import TestCase
from django.contrib.auth.models import User

from courses.models import Course
from accounts.models import Profile


PK = 1


class UserInteractionTest(TestCase):
    def test_can_register(self):
        self.client.post('/accounts/register/',
                         {'username': 'john', 'email': 'john@lennon.com', "password": "johnpassword"})
        user = User.objects.get(username="john")
        self.assertEqual(int(self.client.session[SESSION_KEY]), user.pk)

    def test_login_allow_with_good_cred(self):
        user = User.objects.create_user('john', 'john@lennon.com', 'johnpassword')
        self.client.post('/accounts/login/', {'username': 'john', "password": "johnpassword"})
        self.assertEqual(int(self.client.session[SESSION_KEY]), user.pk)

    def test_login_deny_with_bad_cred(self):
        self.client.post('/accounts/login/', {'username': 'john', "password": "johnpassword"})
        self.assertNotIn(SESSION_KEY, self.client.session)