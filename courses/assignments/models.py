from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Assignment(models.Model):
    number = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
    course = models.ForeignKey("courses.Course")
    week = models.ForeignKey("courses.Week")
    checker_url = models.URLField()

    class Meta:
        unique_together = ('number', 'course', 'week')


class Feedback(models.Model):
    assignment = models.ForeignKey(Assignment)
    student = models.ForeignKey(User)
    attempt = models.PositiveIntegerField()
    mark = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    check_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('assignment', 'student', 'attempt')