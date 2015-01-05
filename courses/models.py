from django.core.validators import RegexValidator
from django.db import models


class Course(models.Model):
    title = models.TextField(unique=True)
    img = models.ImageField(upload_to="courses", default="../media/courses/default.png")
    short_description = models.TextField(default="")
    full_description = models.TextField(default="")


class Week(models.Model):
    course = models.ForeignKey("Course")
    number = models.IntegerField("Number of week")

    class Meta:
        unique_together = ('course', 'number',)


class Lecture(models.Model):
    order_id = models.IntegerField()
    title = models.TextField()
    video_url = models.URLField(
        validators=[RegexValidator(r"^https?:\/\/(www\.)?youtube\.com\/watch\?v\=\S{11}$", "It is not from Youtube")])
    embed_video_url = models.URLField(
        validators=[RegexValidator(r"^https?:\/\/(www\.)?youtube\.com\/embed\/\S{11}$", "Something bad with URL")])

    week = models.ForeignKey("Week")

    class Meta:
        unique_together = ('order_id', 'week',)