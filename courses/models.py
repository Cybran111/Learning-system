from django.core.validators import RegexValidator
from django.db import models


class Course(models.Model):
    title = models.TextField(unique=True)
    img = models.ImageField(upload_to="courses", default="/static/courses/default.png")
    short_description = models.TextField(default="")
    full_description = models.TextField(default="")

    def __unicode__(self):
        return self.title


class News(models.Model):
    course = models.ForeignKey("Course")
    title = models.TextField()
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s (course %d)' % (self.title, self.course_id)


class Week(models.Model):
    course = models.ForeignKey("Course")
    number = models.IntegerField("Number of week")

    class Meta:
        unique_together = ('course', 'number',)

    def __unicode__(self):
        return u'Course %d, number %d' % (self.course_id, self.number)


class Lecture(models.Model):
    order_id = models.IntegerField()
    title = models.CharField(max_length=80)
    video_url = models.URLField(
        validators=[RegexValidator(r"^https?:\/\/(www\.)?youtube\.com\/watch\?v\=\S{11}$", "It is not from Youtube")])
    embed_video_url = models.URLField(
        validators=[RegexValidator(r"^https?:\/\/(www\.)?youtube\.com\/embed\/\S{11}$", "Something bad with URL")])

    week = models.ForeignKey("Week")

    class Meta:
        unique_together = ('order_id', 'week',)
        ordering = ('order_id',)

    def __unicode__(self):
        return u'%s (course %d, week %d, number %d)' % (self.title, self.week.course_id, self.week_id, self.order_id)


class LectureMaterials(models.Model):
    lecture = models.ForeignKey("Lecture")
    title = models.TextField()
    link = models.URLField()

    def __unicode__(self):
        return u'%s (lecture %d, url %s)' % (self.title, self.lecture_id, self.link)