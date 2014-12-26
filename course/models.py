from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.TextField()
    short_description = models.TextField(default="")
    full_description = models.TextField(default="")