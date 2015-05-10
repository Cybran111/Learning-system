# Register your models here.
from django.contrib import admin

from courses.models import Lecture, Course, Week, News, LectureMaterials


admin.site.register((Course, Week, Lecture, News, LectureMaterials))