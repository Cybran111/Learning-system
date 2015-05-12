from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from courses.models import Course


class Profile(models.Model):
    user = models.OneToOneField(User)

    courses = models.ManyToManyField(Course, through='Status')
    # website = models.URLField(blank=True)
    # avatar = models.ImageField(upload_to="avatars", blank=True)

    def __unicode__(self):
        return self.user.username


class Status(models.Model):
    user = models.ForeignKey("Profile")
    course = models.ForeignKey(Course)

    # Student, Teacher or Moderator
    role = models.CharField(max_length=15)

    class Meta:
        unique_together = ('user', 'course')
