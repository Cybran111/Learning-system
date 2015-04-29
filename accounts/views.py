# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from courses.models import Course
from accounts.forms import LoginForm, RegisterForm
from accounts.models import Status, Profile


def home_page(request):
    return render(request, 'dashboard/homepage.html', {"courses": Course.objects.all()})


# TODO: Should be redirected to the enrolled course
@login_required(redirect_field_name="/")
@require_POST
def enroll(request):
    if not Status.objects.filter(course=request.POST['course'], user=request.user.profile, role="student"):
        course = Course.objects.get(pk=request.POST['course'])

        rel = Status(course=course, user=request.user.profile,
                     role="student")
        rel.save()

    return redirect("courses:lectures", (request.POST['course']))


def auth(request):
    # FIXME: notification about bad credentials is not show
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            user = authenticate(username=form.data['username'], password=form.data['password'])
            if user:
                login(request, user)
                return redirect("home")

    else:
        form = LoginForm()
    return render(request, 'dashboard/login.html', {"form": form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            User.objects.create_user(
                username=form.data['username'],
                email=form.data['email'],
                password=form.data['password']
            )

            # Now we save the UserProfile model instance.
            user = authenticate(username=form.data['username'], password=form.data['password'])
            login(request, user)
            Profile.objects.create(user=user)

            return redirect("home")

    else:
        form = RegisterForm()

    return render(request, 'dashboard/register.html', {'form': form})


def profile(request):
    enrolled = Course.objects.filter(profile=request.user.profile).all()
    return render(request, 'dashboard/dashboard.html', {"enrolled": enrolled})
