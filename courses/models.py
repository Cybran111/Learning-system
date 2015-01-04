from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to="courses", default="../media/courses/default.png")
    short_description = models.TextField(default="")
    full_description = models.TextField(default="")


class Week(models.Model):
    course = models.ForeignKey("Course")
    number = models.IntegerField("Number of week")


class Lecture(models.Model):
    title = models.TextField()
    video_url = models.URLField(
        validators=[RegexValidator(r"^https?:\/\/(www\.)?youtube\.com\/watch\S+$", "It is not from Youtube")])
    week = models.ForeignKey("Week")