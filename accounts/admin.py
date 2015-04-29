from django.contrib import admin

# Register your models here.
from accounts.models import Profile, Status

admin.site.register((Profile, Status))