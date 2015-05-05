from django.contrib import admin

# Register your models here.
from courses.assignments.models import Feedback, Assignment

admin.site.register((Assignment, Feedback))