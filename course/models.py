from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to="course", default="../media/course/default.png")
    short_description = models.TextField(default="")
    full_description = models.TextField(default="")