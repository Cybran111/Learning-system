from django.contrib import admin

# Register your models here.
from dashboard.models import Profile, Status

admin.site.register((Profile, Status))